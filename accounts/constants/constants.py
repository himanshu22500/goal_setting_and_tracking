INVALID_USERNAME_FORMAT_MESSAGE = "Invalid username format. Username should start with a letter and can contain 4-20 characters (letters, digits, underscores, and periods)."
INVALID_EMAIL_FORMAT_MESSAGE = "Invalid email format. Email should follow the standard format: local_part@domain.extension."
INVALID_PASSWORD_FORMAT_MESSAGE = "Invalid password format. Password should be 8-20 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character (@$!%*?&)."
USERNAME_REGEX = r"^[a-zA-Z][a-zA-Z0-9._]{3,19}$"
PASSWORD_REGEX = (
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,20}$"
)
EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
CREATE_USER_SUCCESS_MESSAGE = (
    "User created successfully, login with username and password"
)
