from typing import Union

from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
from datetime import date

app = FastAPI()


@app.get("/")
async def read_root():
    return {"result": True}


class User(BaseModel):
    name: str
    email: str
    age: int
    salary: float
    isActive: Union[bool, None] = None
    create_at: date


@app.post("/")
async def store(user: User):
    try:
        return {
            "status": 200,
            "user": user
        }
    except:
        return {
            "status": 400,
            "message": "Error occured"
        }


@app.get("/blocking")
async def queary():
    return {
        "working": True
    }
