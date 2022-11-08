from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import models, schemas
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog', status_code=status.HTTP_200_OK)
def get_blog(db: Session = Depends(get_db)):
    return db.query(models.Blog).all()


@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def get_blog(id:int,response: Response, db: Session = Depends(get_db)):
    # sourcery skip: inline-immediately-returned-variable
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with the {id} is not available'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the {id} is not available')
    return blog


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return {'detail': f'Blog with {id} deleted successfully from db'}


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id:int, request:schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the {id} is not available')
    blog.update(request.dict())
    db.commit()
    return 'updated'
