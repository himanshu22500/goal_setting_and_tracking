# API Documentation

## Endpoint: `GET /user/<int:user_id>/goals`

This endpoint retrieves all public goals of a specific user.

### URL Parameters

- `user_id` (integer): The ID of the user whose public goals you want to retrieve. This is a required parameter.

### Headers

- `Authorization`: The session token of the user making the request. This is required for authentication.

### Response

The response will be a JSON array of public goals. Each goal is represented as a JSON object with the following properties:

- `id` (integer): The ID of the goal.
- `title` (string): The title of the goal.
- `description` (string): The description of the goal.
- `target_datetime` (string): The target completion date and time of the goal in ISO 8601 format.
- `due_datetime` (string): The due date and time of the goal in ISO 8601 format.
- `category` (string): The category of the goal.
- `completed` (boolean): Whether the goal has been completed.
- `is_public` (boolean): Whether the goal is public.
- `priority` (integer): The priority of the goal.
- `update_text` (string): The latest update text of the goal.

### Example Request

```
GET /user/1/goals
Authorization: Bearer <session_token>
```

### Example Response

```json
[
    {
        "id": 1,
        "title": "Learn Python",
        "description": "I want to learn Python for data analysis.",
        "target_datetime": "2023-12-31T23:59:59Z",
        "due_datetime": "2023-12-31T23:59:59Z",
        "category": "Education",
        "completed": false,
        "is_public": true,
        "priority": 1,
        "update_text": "Started learning Python basics."
    },
    {
        "id": 2,
        "title": "Run a marathon",
        "description": "I want to run a marathon in under 4 hours.",
        "target_datetime": "2023-10-01T00:00:00Z",
        "due_datetime": "2023-10-01T00:00:00Z",
        "category": "Fitness",
        "completed": false,
        "is_public": true,
        "priority": 2,
        "update_text": "Started training for the marathon."
    }
]
```

### Error Responses

- `401 Unauthorized`: If the `Authorization` header is missing or invalid.
- `404 Not Found`: If the `user_id` does not correspond to any existing user.
