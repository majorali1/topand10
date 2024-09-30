from typing import List

from db.repository.blog import create_a_new_blog
from db.repository.blog import delete_blog
from db.repository.blog import list_blogs
from db.repository.blog import retrieve_blog
from db.repository.blog import update_a_blog
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from schemas.blogcema import BlogCreate
from schemas.blogcema import BlogUpdate
from schemas.blogcema import ShowBlog
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/blogs", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
async def create_blog(blog: BlogCreate, db: Session = Depends(get_db)):
    blog = create_a_new_blog(blog=blog, db=db, author_id=1)
    return blog


@router.get("/blogs/{id}", response_model=ShowBlog, status_code=status.HTTP_200_OK)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = retrieve_blog(id=id, db=db)
    if not blog:
        raise HTTPException(
            detail=f"Blog with id {id} not found mate.",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return blog


@router.get("/blogs", response_model=List[ShowBlog])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = list_blogs(db=db)
    return blogs


@router.put("/blogs/{id}", response_model=ShowBlog)
def update_blog(id: int, blog: BlogUpdate, db: Session = Depends(get_db)):
    blog = update_a_blog(id=id, blog=blog, db=db, author_id=1)
    if not blog:
        raise HTTPException(detail=f"blog with{id} is not made yet")
    return blog


@router.delete("/delete/{id}")
def delete_a_blog(id: int, db: Session = Depends(get_db)):
    del_message = delete_blog(id=id, author_id=1, db=db)
    if del_message.get("error"):
        raise HTTPException(
            detail=f"blog with id {id} not found",
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    return {"msg": f"blog with id {id} successfully deleted"}
