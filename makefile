# Makefile for building python lambda
PROJECT = vpcbuilder
STACKNAME = VPCBuilder-transform
VERSION = $(shell whoami)
DIR = $(shell pwd)
GITHASH = $(shell git rev-parse HEAD | cut -c 1-7)
BUCKET_NAME = bucket
CONTAINER = python:3.9.6-alpine3.14 
WORKING_DIR = /opt/app
REGION = ap-southeast-2
PROFILE = saml
BUILD_DIR = ./build 
SOURCE_DIR = ./src
TEMPLATE = ./build/template.yaml
SAMTEMPLATE = ./build/sam-template.yaml


genReqs:
	pipenv lock -r > requirements.txt
.PHONY: genReqs

genTestReqs:
	pipenv lock -r --dev > requirements.txt
.PHONY: genTestReqs

buildDeps: genReqs
	docker run -v $(DIR):$(WORKING_DIR) -w $(WORKING_DIR) $(CONTAINER) pip install -r requirements.txt -t ./src
.PHONY: buildDeps

buildPackage:
	cd ./src && zip -r9 ../$(PROJECT).zip *
.PHONY: buildPackage

uploadToS3: buildPackage
	aws s3 cp ./$(PROJECT).zip s3://$(BUCKET_NAME)/$(PROJECT)/$(PROJECT)-$(GITHASH).zip --acl bucket-owner-full-control
	echo 'File version is $(PROJECT)-$(GITHASH).zip'
.PHONY: uploadToS3

testDocker:
	docker build -f Dockerfile.test -t $(PROJECT)-local-test .
.PHONY: testLocal

testLocal:
	PYTHONPATH=.:./src pytest --cov=src --cov-branch --cov-report term-missing ./tests

samBuild: genReqs
	sam build -t .sam/transform.yaml -m ./requirements.txt -b $(BUILD_DIR) -s .
.PHONY: samBuild

samPackage: samBuild
	sam package --template-file $(TEMPLATE) --s3-bucket $(BUCKET_NAME) --output-template-file $(SAMTEMPLATE) --profile $(PROFILE)
.PHONY: samPackage

samDeploy: samPackage
	sam deploy --template-file $(SAMTEMPLATE) --stack-name $(STACKNAME) --capabilities CAPABILITY_IAM --profile $(PROFILE) --region $(REGION)
.PHONY: samDeploy
