from db.models.blog import Blogs
from schemas.blogcema import BlogCreate
from schemas.blogcema import BlogUpdate
from sqlalchemy.orm import Session


def create_a_new_blog(blog: BlogCreate, db: Session, author_id: int = 1):
    blog = Blogs(**blog.model_dump(), author_id=author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def retrieve_blog(id: int, db: Session):
    blog = db.query(Blogs).filter(Blogs.id == id).first()
    return blog


def list_blogs(db: Session):
    blogs = db.query(Blogs).filter(Blogs.is_active == True)
    return blogs


def update_a_blog(id: int, blog: BlogUpdate, db: Session, author_id=int):
    blog_in_db = db.query(Blogs).filter(Blogs.id == id).first()
    if not blog_in_db and blog_in_db != author_id:
        return {"msg": "blog with id {id} not found or you are not the author"}
    blog_in_db.title = blog.title
    blog_in_db.content = blog.content
    db.add(blog_in_db)
    db.commit()
    return blog_in_db


def delete_blog(id: int, db: Session, author_id: int):
    blog_in_db = db.query(Blogs).filter(Blogs.id == id)
    if not blog_in_db.first():
        return {"error": "Sorry the Blog you asked for with id{id }is not available"}
    if blog_in_db.first().author_id != author_id:
        return {"error": "um you are not the author my guy"}
    blog_in_db.delete()
    db.commit()
    return {"msg": "Blog Succesfully Deleted. We hope Your Creativity never fades away"}
