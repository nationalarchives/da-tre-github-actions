#!/bin/bash
cd "${TF_DIR}"
sh ../scripts/init.sh
terraform plan -var-file="terraform.tfvars.json" -input=false -out plan.out -detailed-exitcode > /dev/null 2> error.txt

# If there are no changes then set a VAR and fail
if [ $? -eq 0 ]; then
  echo "::notice::No changes in plan.  Exiting";
  echo "TF_PLAN_CHANGES=0" >> $GITHUB_ENV
  exit 1;
fi
terraform show -no-color plan.out > plan.txt 2> error.txt
aws s3 cp plan.out "${TERRAFORM_PLAN_BUCKET}"/"${ENV}"/"${TRIGGERING_ACTOR}"/ > /dev/null 2> error.txt
