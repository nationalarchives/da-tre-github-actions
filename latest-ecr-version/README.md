## Find the latest pushed container in ECR

This action logs into AWS and obtains one of the following:
 - the tag of the latest pushed container
 - ```0.0``` if no image
 - ```latest``` image if not tagged

## Usage
### Inputs

This action required two inputs.

1. **ecr_registry_path** : The registry name such as ```tre-v2/tna-judgments-parser```
1. **aws_role** : AWS role with permission to perform actions on account ECR

### Outputs

This action produces one output.

1. **latest-version** : The latest version of the container that has been deployed
