FROM python:3.6.2-slim
MAINTAINER Brandon Soto <brandon.soto09@gmail.com>

ADD . /app

WORKDIR /app

EXPOSE 80 8080

RUN apt-get update \
    && apt-get install -y vim \
    && pip install -U praw nltk numpy pyyaml

# TODO(brandon): uncomment this when the app is ready
# CMD ["python", "/app/dogg_giffter.py"]
