#!/bin/bash
set -e


echo
function cleanup {
    status=$?; 
    if [ $status != 0 ] && [ -f error.txt ]; then echo "Failure: $status" && python3 ../scripts/send_to_cw.py error.txt; fi
}

trap cleanup EXIT

ls -la
pwd
cd "${TF_DIR}"
pwd
ls -la
terraform -v
aws ssm get-parameters --name "${AWS_PARAM_STORE_TF_BACKEND_KEY}" --with-decryption --query "Parameters[*].Value" --output text > backend.conf 2> error.txt
aws ssm get-parameters --name "${AWS_PARAM_STORE_TF_VARS_KEY}" --with-decryption --query "Parameters[*].Value" --output text > terraform.tfvars 2> error.txt
terraform init -backend-config=backend.conf -reconfigure > /dev/null 2> error.txt
terraform workspace list
terraform workspace select "${ENV}"
terraform plan -var-file="terraform.tfvars" -input=false -out plan.out > /dev/null 2> error.txt
aws s3 cp s3://dev-te-testdata/tmp/"${ENV}"/"${TRIGGERING_ACTOR}"/plan.out plan.out
terraform show -no-color plan.out > plan.txt
terraform apply -input=false plan.out 2> error.txt