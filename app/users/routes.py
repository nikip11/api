from fastapi import APIRouter, status, HTTPException
from bson import ObjectId
from .schemas import user_schema, users_schema
from .models import User
from .repository import find_user, save_user

from ..core.db import db_client

router = APIRouter(prefix="/users",
                   tags=["users"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})
 
@router.get("/", response_model=list[User])
async def users():
    return users_schema(db_client.users.find())

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def r_save_user(user: User):
    if type(find_user("email", user.email)) == User:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")

    return save_user(user)

@router.get("/{id}")
def r_get_user(id: str):
    user = find_user("_id", ObjectId(id))
    return user_schema(user)
