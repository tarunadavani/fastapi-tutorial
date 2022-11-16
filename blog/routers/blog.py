from typing import List

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from .. import database, schemas, oauth2
from .. repository import blog

router = APIRouter(
    prefix="/blog",
    tags=["Blog"],
)

get_db=database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
def all_blogs(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id: int, response: Response, db: Session = Depends(get_db)):
    return blog.show(id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
   return blog.update(id, request, db)
