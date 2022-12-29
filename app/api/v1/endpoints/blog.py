from typing import List

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.db import database
from app.api import dependencies
from app.schemas import schemas
from app.crud import blog

router = APIRouter()

get_db=database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    return blog.create(request, db, current_user)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
def all_blogs(db: Session = Depends(get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    return blog.get_all(db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id: int, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    return blog.show(id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    return blog.destroy(id, db, current_user)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
   return blog.update(id, request, db, current_user)
