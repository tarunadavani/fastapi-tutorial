from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db import database
from app.api import dependencies
from app.schemas import schemas
from app.crud import user

router = APIRouter()

get_db=database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User,
                db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/', status_code=status.HTTP_200_OK,
        response_model=List[schemas.ShowUser])
def all_users(db: Session = Depends(get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    return user.get_all(db)


@router.get('/{id}', status_code=status.HTTP_200_OK,
        response_model=schemas.ShowUser)
def show_user(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    return user.show(id, db)

