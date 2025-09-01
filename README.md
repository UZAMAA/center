# Student Payment Recorder

This is a simple web application for tracking student payments. It was originally a single-page HTML application and has been converted to a Flask application that uses a JSON file for data persistence.

## Features

- **Create and Manage Grades:** Organize students into grades or classes.
- **Add and Edit Students:** Keep a list of students within each grade.
- **Track Payments:** Record up to 7 payments for each student.
- **Dynamic Interface:** A clean and responsive UI for managing records.

## Project Structure

- `app.py`: The main Flask application file. Contains all backend logic and API endpoints.
- `requirements.txt`: A list of Python dependencies required for the project.
- `data/database.json`: The JSON file used to store all application data.
- `templates/index.html`: The frontend of the application.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Run the Application

1.  **Run the Flask development server:**
    ```bash
    flask run
    ```

2.  **Open your web browser:**
    Navigate to `http://127.0.0.1:5000` to use the application. The app will be running on port 5001 as specified in `app.py`.
