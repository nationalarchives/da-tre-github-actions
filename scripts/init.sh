#!/bin/bash

terraform -v
aws ssm get-parameters --name "${AWS_PARAM_STORE_TF_BACKEND_KEY}" --with-decryption --query "Parameters[*].Value" --output text > backend.conf 2> error.txt
aws ssm get-parameters --name "${AWS_PARAM_STORE_TF_VARS_KEY}" --with-decryption --query "Parameters[*].Value" --output text > terraform.tfvars 2> error.txt
echo "1"
ls -la
terraform init -backend-config=backend.conf -reconfigure > /dev/null 2> error.txt
echo "2"
ls -la
terraform workspace list
terraform workspace select "${ENV}"
echo "3"
ls -la