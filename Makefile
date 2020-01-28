all: 
	docker-compose build && docker-compose up

build:
	docker build -t imflow/url2image .

push: build
	docker push imflow/url2image

dev:
	docker-compose -f docker-compose.dev.yml build && docker-compose -f docker-compose.dev.yml up

test: build
	docker run imflow/url2image bash -c "python3 -m pytest tests"
