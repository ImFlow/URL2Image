[![Build Status](https://travis-ci.org/ImFlow/URL2Image.svg?branch=master)](https://travis-ci.org/ImFlow/URL2Image)
[![Coverage Status](https://coveralls.io/repos/github/ImFlow/URL2Image/badge.svg?branch=master)](https://coveralls.io/github/ImFlow/URL2Image?branch=master)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation Status](https://readthedocs.org/projects/url2image/badge/?version=master)](https://url2image.readthedocs.io/en/master/?badge=master)

# URL2Image
A microservice that turns an URL into an image.
This is a basic working version.

## What it is
URL2Image provides an API, which accepts a URL and returns a rendered image of the URL.

## Installation
Either clone the repo and run it yourself:
```bash
git clone https://github.com/ImFlow/URL2Image.git
```
and then run it via:
```bash 
docker build -t url2image .
docker run -d -p 5000:5000 url2image
```
**or**
use the prebuild docker image:
```bash
docker pull imflow/url2image
docker run -d -p 5000:5000 url2image
```
there is also a `docker-compose.yml` file included so the service can be run using:
```bash
docker-compose up
```

## How To Use
To download an url as a png file call the `/getImage` endpoint.
```bash
curl "localhost:5000/getImage?url=google.de" -o test.png
```

Supported options are `url` to specify the url of the target. This is required. `width`  and `height` are optional parameters specifiing the image dimensions. 
```bash
curl "localhost:5000/getImage?url=google.de&width=400&height=400" -o test.png
```

## TODO
:white_check_mark: Design API

:white_check_mark: Provide API endpoints
- [ ] JWT authentification
- [ ] Username/Password authentification?
- [ ] Configs
- [ ] Image format selection (jpg/png/heif?)

:white_check_mark: DDos protection
