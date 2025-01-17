resource "aws_lambda_function" "lambda_function" {
  function_name    = "user_service"
  runtime          = "python3.9"
  handler          = "user_service.handler"
  role             = aws_iam_role.lambda_exec.arn
  filename         = "lambda/user_service.zip"
  source_code_hash = filebase64sha256("lambda/user_service.zip")
  depends_on = [aws_cloudwatch_log_group.cloudwatch_user_service]
}
