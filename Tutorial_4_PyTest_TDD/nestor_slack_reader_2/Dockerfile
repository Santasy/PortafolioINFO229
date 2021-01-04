FROM python:3.6.3

ENV SLACK_TOKEN="xoxb-1425338835636-1443053375680-gF89z3sQWltu5LuDipH5ltMp"
ENV SLACK_SIGNING_SECRET="9759034b4c7a8ada176b4c27a9ca2687"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /nestor_slack_reader_2

COPY ./nestor_slack_reader_2.py /nestor_slack_reader_2.py

CMD [ "python", "/nestor_slack_reader_2.py" ]
