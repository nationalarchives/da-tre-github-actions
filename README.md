# da-tre-github-actions

Common TRE github actions.

## Actions
| Action | Summary  |
| -----  |----------|
 |[create-ecr-repositoy](create-ecr-repository) | Create an Amazon Elastic container registry ||
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
