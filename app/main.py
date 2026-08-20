from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field


app = FastAPI(
    title="REST API Test Automation Demo",
    description="REST API application used for automated testing",
    version="1.0.0"
)


class User(BaseModel):
    name: str
    email: EmailStr
    age: int = Field(..., ge=18, le=100)


users = [
    {
        "id": 1,
        "name": "Rahul",
        "email": "rahul@example.com",
        "age": 22
    },
    {
        "id": 2,
        "name": "Priya",
        "email": "priya@example.com",
        "age": 23
    }
]


@app.get("/")
def home():
    return {
        "message": "REST API Test Automation Framework"
    }


@app.get("/users")
def get_users():
    return {
        "users": users
    }


@app.post("/users", status_code=201)
def create_user(user: User):
    new_user = {
        "id": len(users) + 1,
        "name": user.name,
        "email": user.email,
        "age": user.age
    }

    users.append(new_user)

    return new_user


@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):


    for existing_user in users:
        if existing_user["id"] == user_id:
            existing_user["name"] = user.name
            existing_user["email"] = user.email
            existing_user["age"] = user.age


            return existing_user


    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


@app.delete("/users/{user_id}")
def delete_user(user_id: int):


    for index, user in enumerate(users):
        if user["id"] == user_id:
            deleted_user = users.pop(index)


            return {
                "message": "User deleted successfully",
                "user": deleted_user
            }


    raise HTTPException(
        status_code=404,
        detail="User not found"
    )