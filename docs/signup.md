# Signup API

## Endpoint

`POST /signup/`

## Description

This API is used to register a new user.

## Request Body

The request body should be a JSON object with the following properties:

- `username` (string): The username of the user. This field is required.
- `email` (string): The email of the user. This field is required.
- `password` (string): The password of the user. This field is required.

## Response

The response will be a JSON object. If the user is registered successfully, the response will have a status code of 200 and contain the following properties:

- `message` (string): A message indicating that the user was registered successfully.
- `data` (object): An object containing the details of the registered user.

If there is an error, the response will have a status code of 400 and contain the following properties:

- `error` (string): A message describing the error.

## Example

### Request

```json
POST /signup/
Content-Type: application/json

{
    "username": "newuser",
    "email": "newuser@example.com",
    "password": "password123"
}
```

### Response

```json
{
    "message": "User created successfully, login with username and password"
}
```
