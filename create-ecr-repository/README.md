## Create an Amazon Elastic Container Registry

This action:
1. Logs into AWS
1. Checks to see if the repository exists
1. Creates the repository if rquired

## Usage
### Inputs

This action required two inputs.

1. **ecr_registry_path** : The repository name such as ```tre-v2/tna-judgments-parser```
1. **aws_role** : AWS role with permission to perform actions on account ECR


### Outputs

This action produces one output.

1. **created** : Returns 1 if created or 0 if it already exists
