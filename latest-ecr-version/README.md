## Find the latest pushed container in ECR

This action logs into AWS and obtains one of the following:
 - the version tag of the latest pushed release container
 - ```0.0.0``` if there is none

Only images with a version number tag (```1.2.3``` or ```v1.2.3```, up to three numbers) are considered.
Other tags, such as ```latest``` or test builds of branches, are ignored.
This action uses ```jq```.

## Usage
### Inputs

This action required two inputs.

1. **ecr_registry_path** : The registry name such as ```tre-v2/tna-judgments-parser```
1. **aws_role** : AWS role with permission to perform actions on account ECR

### Outputs

This action produces one output.

1. **latest-version** : The latest version of the container that has been deployed
