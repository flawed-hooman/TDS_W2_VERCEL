from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json

app = FastAPI()

# Enable CORS for all origins (to allow GET requests from anywhere)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Student marks data
STUDENT_MARKS = [
    {"name": "riUrgLw", "marks": 5},
    {"name": "gJfqNemwRp", "marks": 93},
    {"name": "B0rI", "marks": 21},
    {"name": "ezl1", "marks": 68},
    {"name": "IEV", "marks": 91},
    {"name": "4wO", "marks": 21},
    # Add the rest of your JSON data here...
]

@app.get("/api")
def get_marks(name: List[str] = []):
    """
    Get marks for the requested names.
    Example request: /api?name=riUrgLw&name=B0rI
    Response: {"marks": [5, 21]}
    """
    marks_list = [student["marks"] for student in STUDENT_MARKS if student["name"] in name]
    return {"marks": marks_list}
