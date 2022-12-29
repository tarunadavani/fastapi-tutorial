from app.models import models
from app.schemas import schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.core.hashing import Hash


def get_all(db: Session):
    return db.query(models.User).all()


def create(request: schemas.User, db: Session):
    new_user = models.User(name=request.name, email=request.email, 
                           password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the {id} is not available')
    return user


def get_by_email(email: str, db: Session):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the {email} is not available')
    return user