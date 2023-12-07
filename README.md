# da-tre-github-actions

Common TRE github actions.

## Actions
| Action                                                                           | Summary                                                              |
|----------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [create-ecr-repositoy](create-ecr-repository)                                    | Create an Amazon Elastic container registry                          |
| [update-json-value](update-json-value)                                           | Update JSON value in repository file with signed commit              |
| [repo-check-docker-build-ecr-deploy](repo-check-docker-build-ecr-deploy)         | Create and push container for latest GitHub code                     |
| [docker-build-and-deploy-to-ecr](.github/actions/docker-build-and-deploy-to-ecr) | Build and deploy docker container to ECR                             |
| [version-deployed](version-deployed)                                             | Check if specified version (tag) of container has been deployed      |
| [update-allowed](update-allowed)                                                 | Checks if a specified tag can be used for an automated release       |
| [get-next-version](.github/actions/get-next-version)                             | Get next version                                                     |
| [get-aws-codeartifact-pip-url](.github/actions/get-aws-codeartifact-pip-url)     | Log in to AWS CodeArtifact; saves pip/pypi access URL to named file. |

## Workflows
| Workflow                                                                                                | Summary            |
|---------------------------------------------------------------------------------------------------------|--------------------|
| [Reusable Terraform plan, apply, destroy](.github/workflows/_reusable_terraform_plan_apply_destroy.yml) | Reusable terraform |
| [docker-build-and-ecr-deploy](.github/workflows/docker-build-and-ecr-deploy.yml)                        |Gets next git version tag, builds and deploys Docker image to ECR; if successful, tags git with new version|
| [docker-build-and-ecr-deploy](.github/workflows/docker-build-and-ecr-deploy-using-code-artifact.yml)    |Gets next git version tag, builds and deploys Docker image to ECR; if successful, tags git with new version (Using Code Artifact)|
| [get-and-tag-next-version](.github/workflows/get-and-tag-next-version.yml)                              |Gets next git version and tags repo. For use on merge to main|
| [Court Document Parser CI/CD](.github/workflows/repo-check-docker-build-ecr-deploy.yml)                 |Get latest tag from GitHub reoo. Build docker container and deploy to ECR if required  |
| [on-push-checks](.github/workflows/repo-check-docker-build-ecr-deploy.yml)                              |To do|
| [terraform-environments-action](.github/workflows/tf-plan-approve-apply.yml)                            |To do|
| [terraform-environments-action](.github/workflows/tf-plan.yml)                                          |To do|

### Scala Steward
This workflow runs once per day at 08:15. It runs Scala Steward against all the repositories in [repos.md](./repos.md).

The pull requests are created using the tna-digital-archiving-jenkins user

There is a config file in .github/scala-steward.conf. This is ignoring updates from AWS for now because they release a new patch version every day and this is causing a lot of updates. Once AWS release a new minor version, Scala Steward will create a pull request for that.

## Release History

| Action                                            | Tag   | Summary                                              |
| ------------------------------------------------- | ----- | ---------------------------------------------------- |
| .github/actions/docker-build-and-deploy-to-ecr    | 0.0.1 | Created                                              |
| .github/actions/docker-build-and-deploy-to-ecr    | 0.0.2 | Supports Docker build from AWS CodeArtifact          |
| .github/actions/get-next-version                  | 0.0.1 | Created                                              |
| .github/workflows/docker-build-and-ecr-deploy.yml | 0.0.3 | Created                                              |
| .github/workflows/tf-plan-approve-apply.yml       | 0.0.1 | Created                                              |
| .github/workflows/tf-plan-approve-apply.yml       | 0.0.4 | Allow different manual approval step names (DTE-543) |
| .github/workflows/tf-plan-approve-apply.yml       | 0.0.5 | Capture Apply output (DTE-588 and DTE-544)           |
| .github/workflows/tre-fn-checks.yml               | 0.0.6 | Created (DTE-619)          |                         |
| .github/workflows/tf-plan-approve-apply.yml       | 0.0.7 | Allow PTE creation (DTE-632)                         |
| _reusable_terraform_plan_apply_destroy.yml        | 0.0.8 | Terraform deployment with manual approval (DTE-774)  |
