resource "aws_iam_policy" "example" {
  name        = "example_policy"
  description = "En eksempelpolicy"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action   = "s3:ListBucket"
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}