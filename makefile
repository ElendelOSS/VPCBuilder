# Makefile for building python lambda
PROJECT = vpcbuilder
USER_PROFILE = DevAdmin
VERSION = $(shell whoami)
DIR = $(shell pwd)
GITHASH = $(shell git rev-parse HEAD | cut -c 1-7)
BUCKET_NAME = loopplus-dev-lambdas
CONTAINER = python:2.7.14-alpine3.6
WORKING_DIR = /opt/app

buildDeps:
	docker run -v $(DIR):$(WORKING_DIR) -w $(WORKING_DIR) $(CONTAINER) pip install -r requirements.txt -t ./src
.PHONY: buildDeps

buildPackage:
	cd ./src && zip -r9 ../$(PROJECT).zip *
.PHONY: buildPackage

uploadToS3: buildPackage
	aws s3 cp ./$(PROJECT).zip s3://$(BUCKET_NAME)/$(PROJECT)/$(PROJECT)-$(GITHASH).zip --acl bucket-owner-full-control --profile $(USER_PROFILE)
	echo 'File version is $(PROJECT)-$(GITHASH).zip'
.PHONY: uploadToS3

deployTransform: uploadToS3
	aws --profile $(USER_PROFILE) cloudformation deploy \
		--capabilities CAPABILITY_IAM \
		--template-file transform.yaml \
		--stack-name 'VPC-transform' \
		--parameter-overrides LambdaBucket=$(BUCKET_NAME) LambdaVersion=$(GITHASH)
.PHONY: deployTransform
