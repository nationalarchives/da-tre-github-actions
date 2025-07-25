#!/bin/bash
set -e
cd "${TF_DIR}"
ls -la ../
sh ../scripts/init.sh
aws s3 cp "${TERRAFORM_PLAN_BUCKET}"/"${TRE_ENV}"/"${TRIGGERING_ACTOR}"/plan.out plan.out
terraform apply -no-color -input=false plan.out > apply.out
