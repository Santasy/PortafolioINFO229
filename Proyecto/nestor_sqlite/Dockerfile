FROM python:3.6.3

COPY ./requirements.txt /requirements.txt

ENV PYTHONUNBUFFERED=1

RUN pip install -r /requirements.txt

WORKDIR /nestor_sqlite

COPY ./nestor_sqlite.py /nestor_sqlite.py
COPY ./nestor_sqlite.py /nestor_sqlite.py

CMD [ "python", "/nestor_sqlite.py" ]
