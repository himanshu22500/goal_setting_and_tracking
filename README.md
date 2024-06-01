
# Project Setup Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- virtualenv (Python environment builder)

## Steps

1. **Clone the repository**

    First, you need to clone the repository to your local machine. You can do this with the following command:

    ```bash
    git clone https://github.com/himanshu22500/goal_setting_and_tracking.git
    ```

    Replace `<username>` and `<repository>` with the username and repository name on GitHub.

2. **Create a virtual environment**

    Navigate to the project directory and create a virtual environment using the following command:

    ```bash
    cd goal_setting_and_tracking
    virtualenv venv
    ```

    This will create a new virtual environment in a folder named `venv` in the current directory.

3. **Activate the virtual environment**

    Activate the virtual environment using the following command:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

    You should now see `(venv)` at the beginning of your command line, indicating that you are working inside the virtual environment.

4. **Install the requirements**

    Install the project dependencies using the following command:

    ```bash
    pip install -r requirements.txt
    ```

5. **Apply migrations**

    Apply the Django database migrations using the following command:

    ```bash
    python manage.py migrate
    ```

6. **Run the server**

    Finally, you can run the server using the following command:

    ```bash
    python manage.py runserver
    ```

    The server will start running at `http://127.0.0.1:8000/`.
