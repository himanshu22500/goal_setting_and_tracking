# Get User Goals API

## Endpoint

`GET /api/goals/`

## Description

This API is used to retrieve all goals for a user.

## Request Headers

The request should include the following header:

- `Authorization` (string): The session token of the user. This field is required.

## Response

The response will be a JSON object. If the goals are retrieved successfully, the response will have a status code of 200 and contain the following properties:

- `data` (array): An array of objects, each containing the details of a goal.

Each goal object includes the following fields:

- `id` (string): The unique identifier of the goal.
- `title` (string): The title of the goal.
- `description` (string, optional): A brief description of the goal.
- `target_datetime` (string): The target date and time for the goal in ISO 8601 format.
- `due_datetime` (string, optional): The due date and time for the goal in ISO 8601 format.
- `priority` (integer, optional): The priority of the goal. Higher numbers indicate higher priority.
- `is_public` (boolean, optional): Whether the goal is public or not.

If there is an error, the response will have a status code of 400 or 401 and contain the following properties:

- `error` (string): A message describing the error.

## Example

### Request

```http
GET /api/goals/
Authorization: Bearer abc123
```

### Response

```json
HTTP/1.1 200 OK
Content-Type: application/json

{
    "data": [
        {
            "id": "1",
            "title": "Learn Python",
            "description": "I want to learn Python for data analysis",
            "target_datetime": "2023-01-01T00:00:00Z",
            "due_datetime": "2023-12-31T23:59:59Z",
            "priority": 1,
            "is_public": true
        },
        {
            "id": "2",
            "title": "Learn Django",
            "description": "I want to learn Django for web development",
            "target_datetime": "2023-02-01T00:00:00Z",
            "due_datetime": "2023-12-31T23:59:59Z",
            "priority": 2,
            "is_public": false
        }
    ]
}
```
```json
HTTP/1.1 401 Unauthorized
Content-Type: application/json

{
    "error": "invalid or expired access token"
}
```
