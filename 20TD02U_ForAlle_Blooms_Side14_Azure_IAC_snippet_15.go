package

 test

import (
  "testing"
  "github.com/gruntwork-io/terratest/modules/terraform"
  "github.com/stretchr/testify/assert"
)

func TestTerraformAzureResourceGroup(t *testing.T) {
  terraformOptions := &terraform.Options{
    TerraformDir: "../path_to_your_terraform_code",
  }

  defer terraform.Destroy(t, terraformOptions)

  terraform.InitAndApply(t, terraformOptions)

  output := terraform.Output(t, terraformOptions, "resource_group_name")
  assert.Equal(t, "expected-resource-group-name", output)
}