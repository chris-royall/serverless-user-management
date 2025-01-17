resource "aws_cloudwatch_log_group" "cloudwatch_user_service" {
  name              = "/aws/lambda/user_service"
  retention_in_days = 14
}
