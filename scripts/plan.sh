#!/bin/bash
set -e


echo
function cleanup {
    status=$?; 
    if [ -f error.txt ]; then echo "Failure: $status" && python3 ../scripts/send_to_cw.py error.txt; fi
}

trap cleanup EXIT

ls -la
pwd
cd "${TF_DIR}"
ls -la
sh ../scripts/init.sh
echo "4"
ls -la
terraform plan -var-file="terraform.tfvars" -input=false -out plan.out > /dev/null 2> error.txt
echo "4"
ls -la
terraform show -no-color plan.out > plan.txt
echo "5"
ls -la
echo "${TERRAFORM_PLAN_BUCKET}"
aws s3 cp plan.out "${TERRAFORM_PLAN_BUCKET}"/"${ENV}"/"${TRIGGERING_ACTOR}"/