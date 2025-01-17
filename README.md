# Terraform-Deployed Scalable User Management Service

This project creates infrastructure using IaC Terraform to build a User Management Service. This service demonstrates how to deploy a scalable and serverless backend for managing user data using AWS services. It serves as an example of leveraging AWS Lambda, API Gateway, and DynamoDB in a serverless architecture.

- [Technology Stack](#technology-stack)
- [API](#api)
- [Features](#features)

## Technology Stack

This project leverages the following technologies:
- **DynamoDB**: Used as the primary data store for user data.
- **API Gateway**: Acts as the entry point for the API, routing requests to the appropriate Lambda functions.
- **Lambda**: Processes API requests and interacts with DynamoDB to perform CRUD operations.
- **CloudWatch**: Captures logs for API and Lambda execution, facilitating monitoring and debugging.
- **IAM**: Ensures secure access to AWS resources through role-based policies.

## API

### Create User
```
curl -X PUT -H "Content-Type: application/json" \
-d '{"name": "John Smith"}' "<API_URL>/users?user_id=1"
```

### Retrieve User
```
curl -X GET "<API_URL>/users?user_id=1"

```

### Update User
```
curl -X POST -H "Content-Type: application/json" \
-d '{"user_id": "1", "name": "John Doe"}' <API_URL>/users
```

### Delete User
```
curl -X DELETE "<API_URL>/users?user_id=1"
```


## Features

- **Scalability**: Designed to scale with demand using serverless components.
- **High Availability**: Utilises managed AWS services to ensure high uptime and reliability.
- **Cost Efficiency**: Only pay for what you use with Lambda and DynamoDB on-demand pricing.
- **Extensibility**: Easily extend the system to include more APIs or integrate additional AWS services.

This project highlights the use of modern AWS services to create a reliable and efficient User Management Service. Feel free to explore the Terraform code for detailed configurations.
