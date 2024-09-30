from db.repository.blog import create_a_new_blog
from schemas.blogcema import BlogCreate
from sqlalchemy.orm import Session
from tests.utils.user import create_test_user


def create_test_blog(db: Session):
    blog = BlogCreate(title="Testing", slug="strings", content="Test Content")
    user = create_test_user(db=db)
    blog = create_a_new_blog(blog=blog, db=db, author_id=user.id)
    return blog
