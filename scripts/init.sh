#!/bin/bash
set -e
terraform -v
terraform init -reconfigure
terraform workspace list
terraform workspace select ${TRE_ENV}
