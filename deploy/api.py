from typing import Dict
from pydantic import BaseModel

from fastapi import Depends, FastAPI

from transformers import DistilBertTokenizerFast
from transformers import DistilBertForSequenceClassification
from torch.nn import Softmax
import re

URL_REGEX = re.compile('http(s)?:\/\/t.co\/\w+')
MENTION_REGEX = re.compile('@\w+')


def clean_tweet(tweet):
    # remove mentions, the pound sign, and replace urls with URL token
    tweet = re.sub(URL_REGEX, 'url', tweet)  # replace urls with url. Assumes that the mention of a url is significant
    tweet = re.sub(MENTION_REGEX, '', tweet)  # remove mentions entirely
    tweet = tweet.replace('#', '')  # remove pound signs

    return tweet.strip()


LABELS = {
    0: 'Negative',
    1: 'Neutral',
    2: 'Positive'
}

app = FastAPI()

print("loading tokenizer + model")
tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')
sequence_classification_model = DistilBertForSequenceClassification.from_pretrained(
    'profoz/deploy-mlops-demo', num_labels=3, use_auth_token='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'
)
    # TODO change to './clf/results' for local use

sequence_classification_model.eval()

print("loaded tokenizer + model")


def predict_label(text):
    logits = sequence_classification_model(input_ids=tokenizer.encode(text, return_tensors='pt')).logits
    predicted_label = int(logits.argmax(1).detach())
    label = LABELS[predicted_label]
    return {LABELS[int(i)]: p for i, p in enumerate(Softmax(1)(logits).detach()[0])}, label


class SentimentRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    probabilities: Dict[str, float]
    label: str
    confidence: float


@app.post("/predict", response_model=SentimentResponse)
def predict(request: SentimentRequest):
    probabilities, label = predict_label(clean_tweet(request.text))
    return SentimentResponse(
        label=label, confidence=probabilities[label], probabilities=probabilities
    )
