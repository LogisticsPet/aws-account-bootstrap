# CloudFormation Templates for Terraform Authentication

This repository contains CloudFormation templates for setting up authentication via Terraform Cloud OIDC or GitHub OIDC provider and assuming roles for managing infrastructure. These templates include the definition of the OIDC provider, the role to be assumed, and the necessary policies to create and manage infrastructure resources.

## Templates

The following CloudFormation templates are available:

1. `templates/terraform-cloud.yaml`: This template sets up an OIDC provider, IAM Role and IAM Policy with Required policy set of permissions for Terraform Cloud authentication.
2. `github-oidc-provider.yaml`: This template sets up an OIDC provider, IAM Role and IAM Policy with Required policy set of permissions for GitHub authentication.

## Usage

Ensure that you review and customize the templates according to your specific requirements before deployment.

To use these templates, follow these steps:

1. Create and configure Cloud Formation stacks with Git Sync([AWS docs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/git-sync.html))
2. Update Policy with permissions, when new resources has to be created.


## Note

These templates are designed to be used with AWS CloudFormation. Make sure you have the necessary permissions and resources available in your AWS account to deploy and manage the infrastructure defined by these templates.

For more information on CloudFormation, refer to the [AWS CloudFormation documentation](https://docs.aws.amazon.com/cloudformation/index.html).

