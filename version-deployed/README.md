## Check if a tag version is eligible for release

This action checks if a version bump should be all. The logic is in the ```check_version.sh'''

## Usage
### Inputs

This action required two inputs.

1. **current-tag** : The tag of the version to compare with
1. **new-tag** : The new tag version to check

### Outputs

This action produces no output.

It will **FAIL** if update is not allowed
