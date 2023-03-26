FROM python:3.11.2-buster

ENV PYTHONBUFFERED=1

WORKDIR /photogram

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD gunicorn config.wsgi:application --bind 0.0.0.0:8000

EXPOSE 8000