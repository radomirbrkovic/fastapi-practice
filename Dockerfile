FROM python:3.10-alpine3.13

LABEL mainteiner="radomirbrkovic"

ENV PYTHONUNBUFFERED 1

COPY ./app/requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt

