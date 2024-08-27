package test

import (
  "testing"
  "github.com/gruntwork-io/terratest/modules/terraform"
  "github.com/stretchr/testify/assert"
)

func TestTerraformGCEInstance(t *testing.T) {
  terraformOptions := &terraform.Options{
    TerraformDir: "../path_to_your_terraform_code",
  }

  defer terraform.Destroy(t, terraformOptions)
  terraform.InitAndApply(t, terraformOptions)

  instanceName := terraform.Output(t, terraformOptions, "instance_name")
  assert.Equal(t, "terraform-instance", instanceName)
}