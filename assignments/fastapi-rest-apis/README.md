# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, production-ready REST APIs using the FastAPI framework. Practice creating endpoints, handling HTTP methods, request/response validation, and error handling while building a real-world API application.

## 📝 Tasks

### 🛠️ Set Up FastAPI Application

#### Description
Create a basic FastAPI application with proper project structure and setup. Initialize the project and get a simple endpoint working.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn dependencies
- Create a main application file
- Define a root endpoint (GET /) that returns a welcome message
- Implement at least one additional GET endpoint that returns structured data (e.g., list of items)
- Run the application locally using Uvicorn

### 🛠️ Create CRUD Endpoints

#### Description
Build a complete set of Create, Read, Update, Delete endpoints for managing a resource (e.g., a list of book items, student records, or product inventory).

#### Requirements
Completed program should:

- Implement GET endpoint to retrieve all items
- Implement GET endpoint with path parameter to retrieve a single item by ID
- Implement POST endpoint to create a new item with request body validation
- Implement PUT endpoint to update an existing item
- Implement DELETE endpoint to remove an item
- Use Pydantic models for request/response validation

### 🛠️ Add Error Handling and Validation

#### Description
Enhance the API with proper error handling, input validation, and meaningful error responses.

#### Requirements
Completed program should:

- Validate required fields in request bodies using Pydantic models
- Return appropriate HTTP status codes (200, 201, 400, 404, 500)
- Handle cases where requested items don't exist with 404 responses
- Provide descriptive error messages
- Add type hints to all functions