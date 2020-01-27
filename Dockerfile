FROM python:latest

RUN apt update
RUN apt install -y --no-install-recommends gunicorn

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY url2_image /app/url2_image
COPY ./start.sh /app/
COPY ./configs/gunicorn/gunicorn.conf.py /etc/
COPY ./wsgi.py /app/

WORKDIR /app

CMD ["/app/start.sh"]

