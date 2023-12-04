## Check if a version tag is eligible for release

This action checks if a version bump should be allowed. The logic is in the ```check_version.sh'''

## Usage
### Inputs

This action required two inputs.

- **current-tag** : The tag of the version to compare with
- **new-tag** : The new tag version to check

### Outputs

This action produces no output.

It will **FAIL** if update is not allowed
