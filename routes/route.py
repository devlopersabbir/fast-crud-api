from fastapi import APIRouter
from models.users import User
from configs.database import collectionName
from schema.schemas import index
from bson import objectid

router = APIRouter()

# get all user


@router.get("/")
async def getAllUsers():
    users = index(collectionName.find())
    return users
