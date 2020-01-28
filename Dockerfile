FROM python:latest


RUN apt update
RUN apt install -y --no-install-recommends gunicorn xvfb wget libnss3 libxss1 libappindicator1 libindicator7 libsdl1.2-dev fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 libgtk-3-0 libnspr4 libnss3 libxtst6 lsb-release xdg-utils
WORKDIR /usr/bin
RUN wget https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome*.deb; exit 0

COPY ./requirements.txt /app/requirements.txt
RUN mkdir /tmp_images

RUN pip install -r /app/requirements.txt

COPY url2_image /app/url2_image
COPY ./start.sh /app/
COPY ./configs/gunicorn/gunicorn.conf.py /etc/
COPY ./wsgi.py /app/
COPY ./.git-commit /app/
COPY ./.git-branch /app/
COPY ./tests/ /app/tests/
COPY ./pytest.ini /app/
WORKDIR /app
EXPOSE 5000

ARG GIT_COMMIT=unspecified
LABEL git_commit=$GIT_COMMIT
ENV COMMIT_SHA=${GIT_COMMIT}

CMD ["/app/start.sh"]

