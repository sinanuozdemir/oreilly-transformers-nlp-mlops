# FastAPI Demo

## Installation

1. Make sure you have FastAPI and uvicorn installed (it is in the requirements.txt)


## Running the App
1. From the `deploy` directory, run `uvicorn api:app  --reload` to start your local flask app
2. Test the app by  going to [http://localhost:8000/docs](http://localhost:8000/docs)

## Using Docker

In the `deploy` directory:

to build: `docker build . --tag fastapi-demo:1`

You may need to run with a specified paltform if you use a macbook with the M1 chip like I do: 
`docker build . --tag fastapi-demo:1 --platform linux/amd64`

to run: `docker run -p 80:8000 --platform linux/amd64 fastapi-demo:1`

navigate to [http://localhost/docs](http://localhost/docs)

## To deploy docker image to Heroku
Docs [here](https://devcenter.heroku.com/articles/container-registry-and-runtime)

Tag image for Heroku: `docker tag fastapi-demo:1 registry.heroku.com/oreilly-sinan-mlops/web`

To push to Heroku: `docker push registry.heroku.com/oreilly-sinan-mlops/web`

To release new version: `heroku container:release web -a oreilly-sinan-mlops`

To see logs: `heroku logs -a oreilly-sinan-mlops -t`

Navigate to [https://oreilly-sinan-mlops.herokuapp.com/docs](https://oreilly-sinan-mlops.herokuapp.com/docs)

