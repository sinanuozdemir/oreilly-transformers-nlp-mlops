![oreilly-logo](images/oreilly.png)

# Deploying NLP Models in Production using MLOps

This repository contains code for the [O'Reilly Live Online Training for Deploying NLP Models in Production using MLOps](https://www.oreilly.com/live-events/deploying-nlp-models-in-production-using-mlops/0636920064921/0636920064920)

This training provides an overview to the end-to-end Natural Language Processing pipeline including the initial model training, production deployment and serving, model evaluation, and continuous training cycles to combat model/data drift.

We look at various tools including PyTorch serve and MLflow to manage model versions and deploy them in a production infrastructure. We also see several code examples throughout the training around a semantic search use-case using BERT to help solidify the theoretical concepts being introduced.

### Notebooks

[Model Training/Serving with BERT](notebooks/model_serving.ipynb)

[Model Drift with BERT](notebooks/model_drift.ipynb)

[Deploying models with FastAPI](deploy/)

[Cleaning Data](notebooks/data_cleaning.ipynb)


#### Installation

1. Make sure you have FastAPI and uvicorn installed (it is in the requirements.txt)


#### Running the App
1. From the `deploy` directory, run `uvicorn api:app  --reload` to start your local flask app
2. Test the app by  going to [http://localhost:8000/docs](http://localhost:8000/docs)

##### Using Docker

In the `deploy` directory:

to build: `docker build . --tag fastapi-demo:1`

You may need to run with a specified paltform if you use a macbook with the M1 chip like I do: 
`docker build . --tag fastapi-demo:1 --platform linux/amd64`

to run: `docker run -p 80:8000 --platform linux/amd64 fastapi-demo:1`

navigate to [http://localhost/docs](http://localhost/docs)

### To deploy docker image to Heroku
Docs [here](https://devcenter.heroku.com/articles/container-registry-and-runtime)

Tag image for Heroku: `docker tag fastapi-demo:1 registry.heroku.com/oreilly-sinan-mlops/web`

To push to Heroku: `docker push registry.heroku.com/oreilly-sinan-mlops/web`

To release new version: `heroku container:release web -a oreilly-sinan-mlops`

To see logs: `heroku logs -a oreilly-sinan-mlops -t`

Navigate to [https://oreilly-sinan-mlops.herokuapp.com/docs](https://oreilly-sinan-mlops.herokuapp.com/docs)



## Instructor

*Sinan Ozdemir* is currently the Director of Data Science at Directly, managing the AI and machine learning models that power the company’s intelligent customer support platform. Sinan is a former lecturer of Data Science at Johns Hopkins University and the author of multiple textbooks on data science and machine learning. Additionally, he is the founder of the recently acquired Kylie.ai, an enterprise-grade conversational AI platform with RPA capabilities. He holds a Master’s Degree in Pure Mathematics from Johns Hopkins University and is based in San Francisco, CA.