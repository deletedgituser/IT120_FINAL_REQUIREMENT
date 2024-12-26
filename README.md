# Project Name

![License](https://img.shields.io/github/license/yourusername/your-repo)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contact](#contact)

## Introduction
Welcome to the **Secure Messaging App**!  
This project demonstrates secure communication by employing encryption and decryption of messages. Built with Django and Django REST Framework (DRF), it offers secure APIs, token-based authorization, and user authentication to ensure the confidentiality of messages.

## Features
- **Secure Communication**: Messages are encrypted and decrypted for safe transmission using AES.
- **Token-Based Authorization**: Ensures secure access to API endpoints.
- **User Authentication**: Provides login and secure user management.
- **Modular Design**: Divided into server-side and client-side applications for scalability.

## The project consists of two applications:
1. **server_side**: Provides API endpoints for user registration, login, sending messages, and viewing inbox messages. Also provides admin dashboard to manage users and messages.
2. **client_side**: Interacts with the `server_side` application by making API calls to perform the aforementioned actions.


## Installation
To get started with this project, follow these steps:

### Prerequisites 
Ensure you have Python installed on your system.

### Clone the repository:
    ```sh
    https://github.com/deletedgituser/IT120_FINAL_REQUIREMENT.git
    cd IT120_FINAL_REQUIREMENT
    ```

## Running the server-side application:

### Navigate to the server-side directory:
    ```sh
    cd server_side
    ```

### Activate virtual environment:
    ```sh
    venv\Scripts\activate
    ```

### Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Start server:
    ```sh
    python manage.py runserver
    ```


## Running the client-side application:

### Navigate to the server-side directory:
    ```sh
    cd client_side
    ```

### Activate virtual environment:
    ```sh
    venv\Scripts\activate
    ```

### Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Start server:
    ```sh
    python manage.py runserver 8001
    ```


## Access the Application:
### Open the client application in the browser at:
    ```sh
    http://127.0.0.1:8001/register/
    ```


## API Endpoints
Example API endpoints provided by this project:

- **Register a New User**  
  **POST** `http://127.0.0.1:8000/api/register`  
  Register a new user.

- **Authenticate User**  
  **POST** `http://127.0.0.1:8000/api/login`  
  Authenticate a user and provide a token.

- **Send an Encrypted Message**  
  **POST** `http://127.0.0.1:8000/api/send_message`  
  Send an encrypted message to another user.

- **Retrieve Messages**  
  **GET** `http://127.0.0.1:8000/api/inbox`  
  Retrieve received and sent messages for the authenticated user.

- **Retrieve Users**  
  **GET** `http://127.0.0.1:8000/api/users`  
  Retrieve a list of users to send messages to.


## Contact
For questions or comments about this project, feel free to reach out to any of us:

- **Wendel Rey Salaum**: [wendelreysalaum@gmail.com](mailto:wendelreysalaum@gmail.com)  
  GitHub: [yourusername](https://github.com/yourusername)

- **Member 2**: [member3@example.com](mailto:member2@example.com)  
  GitHub: [member2username](https://github.com/member2username)

- **Member 3**: [member3@example.com](mailto:member3@example.com)  
  GitHub: [member3username](https://github.com/member3username)

- **Member 4**: [member4@example.com](mailto:member4@example.com)  
  GitHub: [member4username](https://github.com/member4username)
