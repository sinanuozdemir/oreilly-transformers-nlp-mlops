![oreilly-logo](images/oreilly.png)

# Deploying NLP Models in Production using MLOps

This repository contains code for the [O'Reilly Live Online Training for Deploying NLP Models in Production using MLOps](https://www.oreilly.com/live-events/deploying-nlp-models-in-production-using-mlops/0636920064921/0636920064920)

This training provides an overview to the end-to-end Natural Language Processing pipeline including the initial model training, production deployment and serving, model evaluation, and continuous training cycles to combat model/data drift.

We look at various tools including PyTorch serve and MLflow to manage model versions and deploy them in a production infrastructure. We also see several code examples throughout the training around a semantic search use-case using BERT to help solidify the theoretical concepts being introduced.

### Notebooks

[Model Drift with BERT](notebooks/model_drift.ipynb)

[Deploying models with FastAPI](deploy/)

[Cleaning Data](notebooks/data_cleaning.ipynb)


#### Installation

1. Make sure you have FastAPI and uvicorn installed (it is in the requirements.txt)


#### Running the App
1. From the `deploy` directory, run `uvicorn api:app  --reload` to start your local flask app
2. Test the app by  going to [http://localhost:8000/docs](http://localhost:8000/docs)

## Instructor

*Sinan Ozdemir* is currently the Director of Data Science at Directly, managing the AI and machine learning models that power the company’s intelligent customer support platform. Sinan is a former lecturer of Data Science at Johns Hopkins University and the author of multiple textbooks on data science and machine learning. Additionally, he is the founder of the recently acquired Kylie.ai, an enterprise-grade conversational AI platform with RPA capabilities. He holds a Master’s Degree in Pure Mathematics from Johns Hopkins University and is based in San Francisco, CA.