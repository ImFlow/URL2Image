FROM python:latest

RUN apt update
RUN apt install -y --no-install-recommends gunicorn

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app

WORKDIR /app

CMD ["/app/start.sh"]

