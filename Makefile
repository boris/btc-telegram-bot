.PHONY: freeze

IMAGE := "111285186890.dkr.ecr.us-east-1.amazonaws.com/telegram-bot"
GIT_COMMIT_HASH := $(shell git rev-parse --short HEAD)
export GIT_COMMIT_HASH

build:
	docker build -t $(IMAGE):$(GIT_COMMIT_HASH) .
	docker push $(IMAGE):$(GIT_COMMIT_HASH)

freeze:
	pip freeze > requirements.txt

run:
	python main.py 

