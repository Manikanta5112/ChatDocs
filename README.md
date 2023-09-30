# ChatDocs
# Chat with your own PDF's

## Introduction

streamlit PDF file upload web app using LLM's

## Running in Docker

To build the image

```
$ docker build . -t chat_app:latest
```

streamlit, by default, runs on port 8501. To run the container (in interactive mode)

```
$ docker run -it -p 8501:8501 chat_app:latest bash

```

or in detached mode

```
$ docker run -d -p 8501:8501 chat_app:latest bash

```
