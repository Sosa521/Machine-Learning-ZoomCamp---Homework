FROM python:3.12-slim

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pip install pipenv

RUN pipenv install --system --deploy

COPY ["predict.py", "model_C=1.0.bin", "./"]
