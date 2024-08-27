aws route53 create-hosted-zone --name example.com --caller-reference "my-unique-string"
   aws route53 change-resource-record-sets --hosted-zone-id Z3M3LMPEXAMPLE --change-batch file://changes.json