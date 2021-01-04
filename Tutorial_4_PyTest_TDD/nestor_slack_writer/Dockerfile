FROM python:3.6.3

ENV SLACK_TOKEN="xoxb-1425338835636-1443053375680-gF89z3sQWltu5LuDipH5ltMp"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /nestor_slack_writer

COPY ./nestor_slack_writer.py /nestor_slack_writer.py
COPY ./nestor_slack_writer.py /nestor_slack_writer.py

CMD [ "python", "/nestor_slack_writer.py" ]
