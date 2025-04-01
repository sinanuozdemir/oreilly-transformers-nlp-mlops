![oreilly-logo](images/oreilly.png)

# Designing and Deploying LLM Pipelines

This repository contains code for the [O'Reilly Live Online Training for Designing and Deploying LLM Pipelines](https://learning.oreilly.com/live-events/designing-and-deploying-llm-pipelines/0642572014796)

In this comprehensive course, machine learning engineers and software developers learn how to transition large language model (LLM) prototypes into fully deployed production systems. Through detailed instruction and real-world case studies, you explore the best practices for integrating LLMs into diverse workflows, ensuring that your models perform effectively in practical applications.

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
