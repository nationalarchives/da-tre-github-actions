## Build and deploy the latest version of lambda docker container to ECR

This action runs a set of actions to
- Check the latest tag of a GitHub repository
- Create an ECR for the container if it does not exist
- Check if the latest GutHub tagged version has been releasede
- Check if the GitHub tagged version should be released
- Build docker container and release to ECR


## Usage

### Inputs

This action requires inputs.

- **repository_name** : The name of the GitHub repository
   - default: ```nationalarchives/tna-judgments-parser```
- **ecr_registry_path** : The ECR name
   - default: ```tre-v2/tna-judgments-parser```
- **docker_file** : The docker file used for the build in the GitHub repository
   - default: ```TRE/DockerfileV2```
- **aws_role** : AWS role with permission to perform actions on account's ECR

### Outputs

This action produces one output.

- **version** : The version of the container that has been deployed
