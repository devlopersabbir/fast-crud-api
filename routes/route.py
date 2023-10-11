from fastapi import APIRouter, status
from models.model import User
from configs.database import usersCollection, movieCollection
from schema.schemas import userSchema, movieSchema, janiNaKiUser
from bson import objectid

router = APIRouter()

# get all user


@router.get("/")
async def getAllUsers():
    return {
        'message': True,
    }
