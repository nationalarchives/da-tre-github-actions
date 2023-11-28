## Check if the tagged container version already exists in Amazon ECR

This action checks if a version bump should be all. The logic is in the ```check_version.sh``` file

## Usage
### Inputs

This action required two inputs.

1. **ecr_registry_path** : ECR path such as ```tre-v2/tna-judgments-parser```
1. **new-tag** : The new tag version to check
1. **aws-role** : AWS role with permissions to read ECR

### Outputs

This action produces one output.

 - **version-deployed** : ```1``` if already deployed
