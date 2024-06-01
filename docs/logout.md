# Logout API

## Endpoint

`POST /logout/`

## Description

This API is used to log out a user, invalidating their current session.

## Request Body

The request body should be a JSON object with the following properties:

- `session_token` (string): The session token of the user. This field is required.

## Response

The response will be a JSON object. If the user is logged out successfully, the response will have a status code of 200 and contain the following properties:

- `message` (string): A message indicating that the user was logged out successfully.

If there is an error, the response will have a status code of 400 and contain the following properties:

- `error` (string): A message describing the error.

## Example

### Request

```json
POST /logout/
Content-Type: application/json

{
    "session_token": "abc123"
}
```

### Response

```json
HTTP/1.1 200 OK
Content-Type: application/json

{
    "message": "User logged out successfully"
}
```

```json
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
    "error": "invalid or expired access token"
}
```
