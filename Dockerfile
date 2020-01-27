FROM python:latest

RUN apt update
RUN apt install -y --no-install-recommends gunicorn

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY URL2Image /app/URL2Image
COPY ./start.sh /app/
COPY ./configs/gunicorn/gunicorn.conf.py /etc/
COPY ./wsgi.py /app/

WORKDIR /app

CMD ["/app/start.sh"]

