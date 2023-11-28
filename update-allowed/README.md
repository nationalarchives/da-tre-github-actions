## Check if the tagged container version already exists in Amazon ECR

This action checks if a version bump should be all. The logic is in the ```check_version.sh``` file

## Usage
### Inputs

This action requires inputs.

 - **ecr_registry_path** : ECR path such as ```tre-v2/tna-judgments-parser```
 - **new-tag** : The new tag version to check
- **aws-role** : AWS role with permissions to read ECR

### Outputs

This action produces one output.

 - **version-deployed** : ```1``` if already deployed
