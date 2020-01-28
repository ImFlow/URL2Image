FROM python:latest


RUN apt update
RUN apt install -y --no-install-recommends gunicorn

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY url2_image /app/url2_image
COPY ./start.sh /app/
COPY ./configs/gunicorn/gunicorn.conf.py /etc/
COPY ./wsgi.py /app/
COPY ./.git-commit /app/git-commit
COPY ./.git-branch /app/git-branch

WORKDIR /app
EXPOSE 5000

ARG GIT_COMMIT=unspecified
LABEL git_commit=$GIT_COMMIT
ENV COMMIT_SHA=${GIT_COMMIT}

CMD ["/app/start.sh"]

