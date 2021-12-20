FROM huggingface/transformers-pytorch-cpu
ENV PYTHONUNBUFFERED 1 

# RUN apk add build-base py3-pip python3-dev rust gcc
RUN pip3 install --upgrade pip

# Expose the port 8000 in which our application runs
EXPOSE 8000 

# Make /app as a working directory in the container
WORKDIR /app 

# Copy requirements to docker container in /app 
COPY ./requirements.txt .

# Copy all files to /app in the container
COPY . . 

# install requirements
RUN pip3 install -r requirements.txt

# Run the application in the port 8000
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "src.api:app"]