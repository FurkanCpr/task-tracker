# Task Tracker Application

A simple task tracking application built with FastAPI backend and Streamlit frontend.

## Features

- Add new tasks
- List existing tasks
- Delete tasks
- Persistent storage with SQLite database

## Technologies

- Backend: FastAPI
- Frontend: Streamlit
- Database: SQLite
- ORM: SQLAlchemy

## Installation

1. Clone the project:
```bash
git clone [repository-url]
cd task-tracker
```

2. Create and activate virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install required packages:
```bash
pip install fastapi uvicorn sqlalchemy streamlit requests
```

## Running the Application

1. Start the backend server:
```bash
uvicorn main:app --reload
```

2. Open a new terminal and start the frontend application:
```bash
streamlit run app.py
```

3. Access the application in your browser at:
- Frontend: http://localhost:8501
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## API Endpoints

- `GET /tasks/`: List all tasks
- `POST /tasks/`: Create a new task
- `GET /tasks/{task_id}`: Get a specific task
- `DELETE /tasks/{task_id}`: Delete a task

