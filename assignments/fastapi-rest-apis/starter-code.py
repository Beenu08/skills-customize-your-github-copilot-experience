# FastAPI REST API Assignment - Starter Code
# Install dependencies: pip install fastapi uvicorn pydantic

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Student Management API", version="1.0.0")

# TODO: Create a Pydantic model for your resource (e.g., Student)
# Example:
# class Student(BaseModel):
#     id: int
#     name: str
#     email: str
#     grade: Optional[str] = None

# TODO: Create an in-memory storage (e.g., a list) for your items
# Example:
# students_db = []

# TODO: Task 1 - Set Up FastAPI Application
# Implement a root GET endpoint that returns a welcome message
@app.get("/")
def read_root():
    """
    Root endpoint - returns welcome message
    """
    return {"message": "Welcome to the Student Management API"}


# TODO: Task 2 - Create CRUD Endpoints
# Implement GET endpoint to retrieve all items
@app.get("/api/items", status_code=status.HTTP_200_OK)
def get_all_items() -> List:
    """
    Retrieve all items
    """
    pass


# Implement GET endpoint with path parameter to retrieve a single item by ID
@app.get("/api/items/{item_id}", status_code=status.HTTP_200_OK)
def get_item(item_id: int):
    """
    Retrieve a single item by ID
    """
    pass


# Implement POST endpoint to create a new item
@app.post("/api/items", status_code=status.HTTP_201_CREATED)
def create_item(item: dict):
    """
    Create a new item
    """
    pass


# Implement PUT endpoint to update an existing item
@app.put("/api/items/{item_id}", status_code=status.HTTP_200_OK)
def update_item(item_id: int, item: dict):
    """
    Update an existing item
    """
    pass


# Implement DELETE endpoint to remove an item
@app.delete("/api/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    """
    Delete an item by ID
    """
    pass


# TODO: Task 3 - Add Error Handling and Validation
# Enhance your endpoints above with:
# - Pydantic model validation for request/response bodies
# - HTTPException with appropriate status codes
# - Meaningful error messages
# - Type hints on all functions

# To run the application:
# uvicorn solution:app --reload
