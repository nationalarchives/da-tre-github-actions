#!/bin/bash
set -e
terraform -v
#aws ssm get-parameters --name "${AWS_PARAM_STORE_TF_BACKEND_KEY}" --with-decryption --query "Parameters[*].Value" --output text > backend.conf 2> error.txt
#aws ssm get-parameters --name "${AWS_PARAM_STORE_TF_VARS_KEY}" --with-decryption --query "Parameters[*].Value" --output text > terraform.tfvars.json 2> error.txt
terraform init -reconfigure > /dev/null 2> error.txt
terraform workspace list 2> error.txt
if $(terraform workspace list 2> error.txt | grep -q "${TRE_ENV}") ; then \
    terraform workspace select ${TRE_ENV} 2> error.txt;
else
    terraform workspace new ${TRE_ENV} 2> error.txt;
    echo "New workspace ${TRE_ENV} created"
fi
