# Python Crowd Funding Console App
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/mohammed-hamdi26/python-Crowd-Funding-console-app)

## About The Project

This is a simple, console-based application for managing crowd-funding projects. It provides a command-line interface (CLI) for users to register, log in, and perform full CRUD (Create, Read, Update, Delete) operations on their funding campaigns. All user and project data is persisted locally using JSON files.

## Features

*   **User Authentication**: Securely register a new account and log in. User sessions are managed for the duration of the application's runtime.
*   **Project Management**:
    *   **Create**: Add new crowd-funding projects with a title, description, total target, start date, and end date.
    *   **View**: Display a formatted list of all projects created by the currently logged-in user.
    *   **Update**: Modify the details of an existing project.
    *   **Delete**: Remove a project from the system.
*   **Data Persistence**: All data is saved to and loaded from local `json` files, ensuring data is not lost between sessions.
*   **Input Validation**: The application validates email formats and Egyptian mobile phone numbers upon registration to ensure data integrity.

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

*   Python 3.x installed on your system.

### Installation & Usage

1.  Clone the repository to your local machine:
    ```sh
    git clone https://github.com/mohammed-hamdi26/python-crowd-funding-console-app.git
    ```
2.  Navigate to the project directory:
    ```sh
    cd python-crowd-funding-console-app
    ```
3.  Run the application from your terminal:
    ```sh
    python main.py
    ```

## How It Works

Upon starting the application, you are greeted with the main menu where you can either log in or register a new account.

```
Welcome to the Project Management System!
==========================================
1. Login
2. Register
Enter your choice:
```

After a successful login, you gain access to the project management dashboard, allowing you to manage your crowd-funding campaigns.

```
1. Create Project
2. View Projects
3. Update Project
4. Delete Project
5. Logout
6. Exit
Enter your choice:
```

## Project Structure

The codebase is organized to separate concerns, making it modular and easy to understand.

```
├── main.py               # Main application entry point and UI logic
├── json/
│   ├── projects.json     # Database for projects
│   └── users.json        # Database for users
├── models/
│   ├── project.py        # Project data model
│   └── user.py           # User data model
├── services/
│   ├── auth_service.py   # Handles user authentication logic
│   └── project_service.py# Handles project CRUD logic
└── utils/
    ├── file_handler.py   # Helper functions for reading/writing JSON files
    └── validation.py     # Helper functions for input validation