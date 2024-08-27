package test

import (
  "testing"
  "github.com/gruntwork-io/terratest/modules/terraform"
  "github.com/stretchr/testify/assert"
)

func TestTerraformS3Bucket(t *testing.T) {
  terraformOptions := &terraform.Options{
    TerraformDir: "../path_to_your_terraform_code",
  }

  defer terraform.Destroy(t, terraformOptions)
  terraform.InitAndApply(t, terraformOptions)

  bucketID := terraform.Output(t, terraformOptions, "bucket_id")
  assert.NotEmpty(t, bucketID)
}