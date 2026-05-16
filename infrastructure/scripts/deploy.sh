#!/bin/bash

STACK_NAME=lakepulse-base-stack

aws cloudformation deploy \
  --template-file ../cloudformation/base-infra.yaml \
  --stack-name $STACK_NAME \
  --capabilities CAPABILITY_NAMED_IAM