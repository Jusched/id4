# 4ID Login/Logout with FastAPI

## Introduction

This is a FastAPI application that provides endpoints for user signup and logout.

## Prerequisites

- Python 3.6+

## Usage

1. Clone the repository by executing `git clone https://github.com/Jusched/id4.git`
2. Go to the project folder by running `cd id4`
3. Create a virtual environment to avoid installing packages globally with `python3 -m venv venv`
4. Activate your virtual environment by running `source venv/bin/activate` in your Terminal.
5. Install the required packages by running `pip install -r requirements.txt`
6. Run the application by executing `uvicorn main:app --reload`
7. Signup a user by making a `POST` request to `localhost:8000/signup` with a JSON payload containing `email` and `password`. The `email` must be unique and the `password` must be longer than 8 characters.
8. Logout a user by making a `POST` request to `localhost:8000/logout` with a JSON payload containing the `email` of the user.

## Endpoints

- `/signup`: This endpoint is used to register a new user. It accepts a JSON payload containing the user's `email` and `password`. Upon successful signup, the registered user's information will be returned in a JSON object.
- `/logout`: This endpoint is used to log out a user. It accepts a JSON payload containing the user's `email`. A successful logout will result in a message confirming that the user has been logged out.
- `/clear`: This endpoint is used to clear the database.

## Note

It's important to note that before the password is stored in the database, it's encrypted using the `encrypt_password()` utility for added security.
