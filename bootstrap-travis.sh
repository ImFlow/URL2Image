#!/bin/bash

sudo apt update
sudo apt install -y --no-install-recommends gunicorn xvfb wget libnss3 libxss1 libappindicator1 libindicator7 libsdl1.2-dev fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 libgtk-3-0 libnspr4 libnss3 libxtst6 lsb-release xdg-utils enchant
cd /usr/bin
sudo wget https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip
sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && sudo dpkg -i google-chrome*.deb


sudo mkdir /tmp_images
sudo chmod a+rwx /tmp_images

pip install -r requirements.txt
pip install pytest pytest-cov coveralls pyenchant
ls -alsh