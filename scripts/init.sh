#!/bin/bash
set -e
terraform -v
aws ssm get-parameters --name "${AWS_PARAM_STORE_TF_BACKEND_KEY}" --with-decryption --query "Parameters[*].Value" --output text > backend.conf 2> error.txt
aws ssm get-parameters --name "${AWS_PARAM_STORE_TF_VARS_KEY}" --with-decryption --query "Parameters[*].Value" --output text > terraform.tfvars.json 2> error.txt
terraform init -backend-config=backend.conf -reconfigure > /dev/null 2> error.txt
terraform workspace list 2> error.txt
if $(terraform workspace list 2> error.txt | grep -q "${TF_WORKSPACE}") ; then \
    terraform workspace select ${TF_WORKSPACE} 2> error.txt;
else 
    terraform workspace new ${TF_WORKSPACE} 2> error.txt;
fi
