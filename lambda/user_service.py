import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

def handler(event, context):
    try:
        http_method = event['httpMethod']
        # Only parse the body for methods that require it
        body = json.loads(event.get('body', '{}')) if http_method in ['POST', 'PUT'] and 'body' in event else None
        # Extract query parameters for GET method
        user_id = event.get('queryStringParameters', {}).get('user_id') if event.get('queryStringParameters') else None

        # Check the http method
        if http_method == 'POST':  # Create
            return create_user(body)
        elif http_method == 'GET':  # Read
            return get_user(user_id)
        elif http_method == 'PUT':  # Update
            return update_user(user_id, body)
        elif http_method == 'DELETE':  # Delete
            return delete_user(user_id)
        else:
            return {
                "statusCode": 405,
                "body": json.dumps({"error": "Method Not Allowed"})
            }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

def create_user(body):
    if not body or not body.get('user_id') or not body.get('email') or not body.get('first_name') or not body.get('last_name') or not body.get('date_of_birth') or not body.get('location'):
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "user_id, email, first_name, last_name, date_of_birth, and location are required"})
        }

    table.put_item(Item={
        "user_id": body['user_id'],
        "email": body['email'],
        "first_name": body['first_name'],
        "last_name": body['last_name'],
        "date_of_birth": body['date_of_birth'],
        "location": body['location']
    })

    return {
        "statusCode": 201,
        "body": json.dumps({"message": "User created successfully"})
    }

def get_user(user_id):
    if not user_id:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "user_id is required"})
        }

    response = table.get_item(Key={"user_id": user_id})
    if 'Item' not in response:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": "User not found"})
        }

    return {
        "statusCode": 200,
        "body": json.dumps(response['Item'])
    }

def update_user(user_id, body):
    if not user_id or not body:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "user_id and update data are required"})
        }

    update_expression = "SET " + ", ".join(f"#{k} = :{k}" for k in body.keys())
    expression_attribute_names = {f"#{k}": k for k in body.keys()}
    expression_attribute_values = {f":{k}": v for k, v in body.items()}

    table.update_item(
        Key={"user_id": user_id},
        UpdateExpression=update_expression,
        ExpressionAttributeNames=expression_attribute_names,
        ExpressionAttributeValues=expression_attribute_values,
        ReturnValues="ALL_NEW"
    )
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "User updated successfully"})
    }

def delete_user(user_id):
    if not user_id:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "user_id is required"})
        }

    table.delete_item(Key={"user_id": user_id})
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "User deleted successfully"})
    }
