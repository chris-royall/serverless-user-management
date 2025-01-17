

```
curl -X POST -H "Content-Type: application/json" \
-d '{"user_id": "1", "name": "John Doe"}' <API_URL>/users
```

```
curl -X GET "<API_URL>/users?user_id=1"

```

```
curl -X PUT -H "Content-Type: application/json" \
-d '{"name": "John Smith"}' "<API_URL>/users?user_id=1"
```

```
curl -X DELETE "<API_URL>/users?user_id=1"
```
