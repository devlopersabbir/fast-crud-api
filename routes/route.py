from fastapi import APIRouter, status
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

# create new user


@router.post("/")
async def createUser(user: User):
    try:
        print(user.email)
        print("================")
        collectionName.insert_one(dict(user))
        return {
            "message": "user created successfully!",
            "user": user
        }
    except Exception as error:
        print(error)
        return {
            "message": "Something went wrong!",
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "error": error
        }
