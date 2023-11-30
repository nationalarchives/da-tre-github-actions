## Updates a json value in a file, to a branch with a signed commit

This action runs a set of actions to
- Check the latest tag of a GitHub repository
- Create an ECR for the container if it does not exist
- Check if the latest GutHub tagged version has been released
- Check if the GitHub tagged version should be released
- Build docker container and release to ECR


## Usage

### Inputs

This action requires inputs.

 - **file_name** : Name of the file to update
 - **field** : JSON field/key to update
 - **value** : The new value
 - **gpg_private_key** : GPG key for signed commit
 - **gpg_passphrase** : GPG passphrase for signed commit
 - **github_token** : Calling workflows GitHub token ```secrets.GITHUB_TOKEN ```

### Outputs

This action produces one output.

 - **branch** : The name of the branch created for the update commit
