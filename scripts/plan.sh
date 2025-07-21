#!/bin/bash
cd "${TF_DIR}"
ls -la ../
sh ../scripts/init.sh
terraform plan -no-color -detailed-exitcode -input=false -var-file="terraform.tfvars.json" -out plan.out
TF_EXIT_CODE=$?
echo "TF exited with ${TF_EXIT_CODE}"

# If there are no changes then set a VAR and fail
if [ $TF_EXIT_CODE -eq 0 ]; then
  echo "::notice::No changes in plan.  Exiting";
  echo "TF_PLAN_CHANGES=0" >> $GITHUB_ENV
  exit 1;
fi

# If Terraform errors
if [ $TF_EXIT_CODE -eq 1 ]; then
  echo "::error::Terraform exited 1.  Exiting";
  exit 1;
fi

set -e
terraform show -no-color plan.out
aws s3 cp plan.out "${TERRAFORM_PLAN_BUCKET}"/"${TRE_ENV}"/"${TRIGGERING_ACTOR}"/
