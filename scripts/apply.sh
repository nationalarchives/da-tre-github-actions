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
sh ../scripts/init.sh
terraform plan -var-file="terraform.tfvars.json" -input=false -out plan.out > /dev/null 2> error.txt
aws s3 cp "${TERRAFORM_PLAN_BUCKET}"/"${ENV}"/"${TRIGGERING_ACTOR}"/plan.out plan.out > /dev/null 2> error.txt
terraform apply -input=false plan.out > apply.out 2> error.txt