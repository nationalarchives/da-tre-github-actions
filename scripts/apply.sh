#!/bin/bash
set -e
cd "${TF_DIR}"
sh ../scripts/init.sh
terraform plan -var-file="terraform.tfvars.json" -no-color -input=false -out plan.out > /dev/null 2> error.txt
aws s3 cp "${TERRAFORM_PLAN_BUCKET}"/"${ENV}"/"${TRIGGERING_ACTOR}"/plan.out plan.out > /dev/null 2> error.txt
terraform apply -no-color -input=false plan.out > apply.out 2> error.txt
