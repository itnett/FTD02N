func TestTerraformModule(t *testing.T) {
       terraformOptions := &terraform.Options{
           TerraformDir: "../path_to_your_module",
       }

       defer terraform.Destroy(t, terraformOptions)

       terraform.InitAndApply(t, terraformOptions)

       output := terraform.Output(t, terraformOptions, "instance_ip")
       assert.NotEmpty(t, output)
   }