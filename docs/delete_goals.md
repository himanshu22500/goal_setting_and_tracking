# Delete Goal API

## Endpoint

`DELETE /api/goals/<str:goal_id>/delete`

## Description

This API is used to delete a specific goal for a user.

## Request Parameters

The request should include the following parameter:

- `goal_id` (string): The unique identifier of the goal. This field is required.

## Request Headers

The request should include the following header:

- `Authorization` (string): The session token of the user. This field is required.

## Response

The response will be a JSON object. If the goal is deleted successfully, the response will have a status code of 200 and contain the following properties:

- `message` (string): A message indicating that the goal was deleted successfully.

If there is an error, the response will have a status code of 400, 401 or 404 and contain the following properties:

- `error` (string): A message describing the error.

## Example

### Request

```http
DELETE /api/goals/1/delete
Authorization: Bearer abc123
```

### Response

```json
HTTP/1.1 200 OK
Content-Type: application/json

{
    "message": "goal deleted successfully"
}
```
```json
HTTP/1.1 401 Unauthorized
Content-Type: application/json

{
    "error": "invalid or expired access token"
}
```
```json
HTTP/1.1 404 Not Found
Content-Type: application/json

{
    "error": "goal not found"
}
```
