# Login API

## Endpoint

`POST /login/`

## Description

This API is used to authenticate a user.

## Request Body

The request body should be a JSON object with the following properties:

- `username` (string): The username of the user. This field is required.
- `password` (string): The password of the user. This field is required.

## Response

The response will be a JSON object. If the user is authenticated successfully, the response will have a status code of 200 and contain the following properties:

- `message` (string): A message indicating that the user was authenticated successfully.
- `data` (object): An object containing the details of the authenticated user and the session token.

If there is an error, the response will have a status code of 400 and contain the following properties:

- `error` (string): A message describing the error.

## Example

### Request

```json
POST /api/login/
Content-Type: application/json

{
    "username": "existinguser",
    "password": "password123"
}

HTTP/1.1 200 OK
Content-Type: application/json
```

### Response

```json
{
  "access_token": "session_token"
}
```

```json
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
    "error": "Invalid username or password"
}
```
