# ToDo App Backend

## Overview
This repository contains the backend of a ToDo application built using **FastAPI**, a modern, fast (high-performance) web framework for Python. It provides RESTful APIs for managing tasks, including creating, reading, updating, and deleting ToDo items. The project also includes complete endpoint testing to ensure the reliability and functionality of all API endpoints.

---

## Features
- User authentication (JWT-based).
- CRUD operations for ToDo items.
- Filtering and sorting of ToDo items.
- Pagination support.
- Complete endpoint testing with Pytest.
- Robust error handling and input validation.

---

## Technology Stack
- **Framework:** FastAPI
- **Database:** Postgres
- **ORM:** SQLAlchemy
- **Testing:** Pytest
- **Authentication:** JWT

---

## Installation

### Prerequisites
- Python 3.9+
- pip (Python package manager)

The API will be available at `http://127.0.0.1:8000`.

---

## Endpoints

### Authentication
- **POST** `/auth/register`: Register a new user.
- **POST** `/auth/login`: Authenticate and obtain a JWT token.

### ToDo Items
- **GET** `/todos`: Retrieve a list of all ToDo items.
- **GET** `/todos/{id}`: Retrieve details of a specific ToDo item.
- **POST** `/todos`: Create a new ToDo item.
- **PUT** `/todos/{id}`: Update an existing ToDo item.
- **DELETE** `/todos/{id}`: Delete a ToDo item.

---

## Testing

### Run Tests
To run the tests, execute the following command:
```bash
pytest
```

### Test Features
- Unit tests for utility functions.
- Integration tests for all API endpoints using HTTPX.
- Database setup and teardown for test isolation.
- JWT authentication testing.

---

## Configuration

Environment variables can be configured in a `.env` file. Below are the default configurations:

```env
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Directory Structure
```
.
├── app
│   ├── cruds
│   │   ├── todo_crud.py
│   │   ├── user_crud.py
│   ├── models
│   │   ├── todo_model.py
│   │   ├── user_model.py
│   ├── router
│   │   ├── auth_router.py
│   │   ├── todo_router.py
│   ├── schema
│   │   ├── todo_schema.py
│   │   ├── user_schema.py
├── main.py
├── requirements.txt
├── README.md
```

---

## Future Enhancements
- Add support for user roles and permissions.
- Implement soft delete for ToDo items.
- Add WebSocket support for real-time updates.
- Deploy the application to a cloud platform (AWS, Azure, GCP).

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
