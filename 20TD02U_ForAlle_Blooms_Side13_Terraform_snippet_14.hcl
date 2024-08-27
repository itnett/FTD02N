import "tfplan/v2" as tfplan

main = rule {
  all tfplan.resource_changes as _, resource {
    resource.applied.outcome is "create"
    resource.applied_type is "aws_s3_bucket"
    resource.applied.values.logging != null
  }
}