## Build and deploy the latest version of lambda docker container to ECR

This action runs a set of actions to
- Check the latest tag of a GitHub repository
- Create an ECR for the artifact if it does not exist
- Check if the version in ECR (Tag in ECR and GitHub tag same
- Check if the GitHub tag version should be released
- Build docker container and release to ECR-


## Usage

### Inputs

This action required four inputs.

1. **repository_name** : The name of the GitHub repository
   - default: ```nationalarchives/tna-judgments-parser```
1. **ecr_registry_path** : The ECR name
   - default: ```tre-v2/tna-judgments-parser```
1. **docker_file** : The docker file used for the build in the GitHub repository
   - default: ```TRE/DockerfileV2```
1. **aws_role** : AWS role with permission to perform actions on account ECR

### Outputs

This action produces one output.

1. **version** : The version of the artifact that has been deployed
