resource "aws_s3_bucket" "bucket" {
     bucket = "min-bucket"
     acl    = "private"
   }