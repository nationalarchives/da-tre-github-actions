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
ls -la
sh ../scripts/init.sh
terraform plan -var-file="terraform.tfvars" -input=false -out plan.out > /dev/null 2> error.txt
terraform show -no-color plan.out > plan.txt
aws s3 cp plan.out "${TERRAFORM_PLAN_BUCKET}"/"${ENV}"/"${TRIGGERING_ACTOR}"/ > /dev/null 2> error.txt