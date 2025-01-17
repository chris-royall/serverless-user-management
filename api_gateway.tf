resource "aws_apigatewayv2_api" "user_api" {
  name          = "user_service_api"
  protocol_type = "HTTP"
}

resource "aws_apigatewayv2_integration" "lambda_integration" {
  api_id           = aws_apigatewayv2_api.user_api.id
  integration_type = "AWS_PROXY"
  integration_uri  = aws_lambda_function.lambda_function.invoke_arn
}

resource "aws_apigatewayv2_stage" "default_stage" {
  api_id      = aws_apigatewayv2_api.user_api.id
  name        = "$default"
  auto_deploy = true
}

resource "aws_lambda_permission" "api_gateway_permission" {
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda_function.function_name
  principal     = "apigateway.amazonaws.com"
  statement_id  = "AllowAPIGatewayInvoke"
}

resource "aws_apigatewayv2_route" "authorized_post_route" {
  api_id            = aws_apigatewayv2_api.user_api.id
  route_key         = "POST /users"
  target            = "integrations/${aws_apigatewayv2_integration.lambda_integration.id}"
}

resource "aws_apigatewayv2_route" "authorized_get_route" {
  api_id            = aws_apigatewayv2_api.user_api.id
  route_key         = "GET /users"
  target            = "integrations/${aws_apigatewayv2_integration.lambda_integration.id}"
}

resource "aws_apigatewayv2_route" "authorized_delete_route" {
  api_id            = aws_apigatewayv2_api.user_api.id
  route_key         = "DELETE /users"
  target            = "integrations/${aws_apigatewayv2_integration.lambda_integration.id}"
}

resource "aws_apigatewayv2_route" "authorized_put_route" {
  api_id            = aws_apigatewayv2_api.user_api.id
  route_key         = "PUT /users"
  target            = "integrations/${aws_apigatewayv2_integration.lambda_integration.id}"
}
