from db.base import Blogs
from tests.utils.blog import create_test_blog


def test_blog_fetcher(client, db_session):
    blog = create_test_blog(db=db_session)
    fetched_blog = db_session.query(Blogs).filter_by(id=blog.id).first()
    assert fetched_blog is not None, "The blog should exist in the database"
    response = client.get(f"blogs/{blog.id}/")
    assert response.status_code == 200
    assert response.json()["title"] == blog.title
