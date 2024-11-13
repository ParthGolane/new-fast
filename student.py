from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os


MONGO_URL = "mongodb://localhost:27017"  # replace with your MongoDB connection string
DATABASE_NAME = "school_db"
COLLECTION_NAME = "students"

app = FastAPI()
client = AsyncIOMotorClient(MONGO_URL)
db = client[DATABASE_NAME]
student_collection = db[COLLECTION_NAME]


class Student(BaseModel):
    id: int
    name: str


@app.post("/students/", response_model=dict)
async def add_student(student: Student):
    student_data = student.dict()
    existing_student = await student_collection.find_one({"id": student.id})

    if existing_student:
        raise HTTPException(status_code=400, detail="Student with this ID already exists")

    result = await student_collection.insert_one(student_data)
    return {"message": "Student added", "student_id": str(result.inserted_id)}


@app.get("/students/{student_id}", response_model=Student)
async def get_student(student_id: int):
    student_data = await student_collection.find_one({"id": student_id})
    if student_data is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return Student(id=student_data["id"], name=student_data["name"])
