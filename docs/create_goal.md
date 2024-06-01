# Create Goal API

## Endpoint

`POST /api/goal/`

## Description

This API is used to create a new goal for a user.

## Request Body

The request body should be a JSON object with the following properties:

- `title` (string): The title of the goal. This field is required.
- `description` (string, optional): A brief description of the goal.
- `category` (string): The category of the goal. This field is required.
- `target_datetime` (string): The target date and time for the goal in ISO 8601 format. This field is required.
- `due_datetime` (string, optional): The due date and time for the goal in ISO 8601 format.
- `priority` (integer, optional): The priority of the goal. Higher numbers indicate higher priority.
- `is_public` (boolean, optional): Whether the goal is public or not.
- `session_token` (string): The session token of the user. This field is required.

## Response

The response will be a JSON object. If the goal is created successfully, the response will have a status code of 200 and contain the following properties:

- `message` (string): A message indicating that the goal was created successfully.
- `data` (object): An object containing the details of the created goal.

If there is an error, the response will have a status code of 400 and contain the following properties:

- `error` (string): A message describing the error.

## Example

### Request

```json
POST /goal/
Content-Type: application/json

{
    "title": "Learn Python",
    "description": "I want to learn Python for data analysis",
    "category": "Education",
    "target_datetime": "2023-01-01T00:00:00Z",
    "due_datetime": "2023-12-31T23:59:59Z",
    "priority": 1,
    "is_public": true,
    "session_token": "abc123"
}
```

### Request
```json
HTTP/1.1 200 OK
Content-Type: application/json

{
    "message": "goal created successfully",
    "data": {
        "id": 1,
        "title": "Learn Python",
        "description": "I want to learn Python for data analysis",
        "target_datetime": "2023-01-01T00:00:00Z",
        "due_datetime": "2023-12-31T23:59:59Z",
        "priority": 1,
        "is_public": true
    }
}
```
