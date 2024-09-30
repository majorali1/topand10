from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import field_validator


class BlogCreate(BaseModel):
    title: str
    slug: Optional[str] = None
    content: Optional[str] = None

    @field_validator("slug", mode="before")
    def generate_slug(cls, slug, values):
        values = slug
        if "title" in values:
            slug["slug"] = values.get("title").replace(" ", "-").lower()
        return slug


class ShowBlog(BaseModel):
    title: str
    content: Optional[str]
    created_at: datetime

    class ConfigDict:
        from_attributes = True


class BlogUpdate(BlogCreate):
    pass
