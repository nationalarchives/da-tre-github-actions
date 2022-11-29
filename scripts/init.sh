#!/bin/bash

terraform -v
aws ssm get-parameters --name "${AWS_PARAM_STORE_TF_BACKEND_KEY}" --with-decryption --query "Parameters[*].Value" --output text > backend.conf 2> error.txt
aws ssm get-parameters --name "${AWS_PARAM_STORE_TF_VARS_KEY}" --with-decryption --query "Parameters[*].Value" --output text > terraform.tfvars 2> error.txt
terraform init -backend-config=backend.conf -reconfigure > /dev/null 2> error.txt
terraform workspace list > /dev/null 2> error.txt
terraform workspace select "${ENV}" > /dev/null 2> error.txt