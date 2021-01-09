FROM python:3.6.3

COPY ./requirements.txt /requirements.txt

RUN pip install --upgrade pip

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /nestor_translate_es_en

COPY ./nestor_translate_es_en.py /nestor_translate_es_en.py

CMD [ "python", "/nestor_translate_es_en.py" ]
