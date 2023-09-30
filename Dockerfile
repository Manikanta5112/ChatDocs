# Use an official python runtime as a parent image
FROM python:3.11

# set the working directory to /app
WORKDIR /app

# copy the current directory content into the container at /app
COPY ./dashboard.py /app/
COPY ./requirements.txt /app/

# Install needed packages in requirements.txt
RUN pip install -r requirements.txt && rm requirements.txt
RUN echo "deb http://deb.openjdk.java.net/debian buster main" > /etc/apt/sources.list
RUN apt-get update && apt-get install openjdk-17-jdk -y

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

CMD [ "streamlit","run","dashboard.py" ]


