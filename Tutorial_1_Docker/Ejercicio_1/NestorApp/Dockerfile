FROM python:latest

ENV MONGO_HOST localhost
ENV MONGO_PORT 27017

# Esto se declara, pero fue dejado en blanco para git
ENV SLACKBOT_TOKEN="" 
# ENV SLACK_EVENTS_TOKEN=""
# -----------------------

COPY ./requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt

WORKDIR /NestorApp

COPY ./nestorbot.py /nestorbot.py
COPY ./nestorbot_app.py /nestorbot_app.py
COPY ./nestorbot_tests.py /nestorbot_tests.py

CMD [ "python", "/nestorbot_app.py" ]