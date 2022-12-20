from .. import models, schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException, status


def get_all(db: Session):
    return db.query(models.Blog).all()


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return {'detail': f'Blog with {id} deleted successfully from db'}


def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the {id} is not available')
    blog.update(request.dict())
    db.commit()
    return 'updated'


def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with the {id} is not available'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the {id} is not available')
    return blog


# deployment docker
# postgres
# pass multiple query parameters 
# only created user can delete, update permission
# how to generate multiple models autogenerate
# run with python command