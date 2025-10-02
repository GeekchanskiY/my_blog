from db import Session
from model.models import BlogItem

class BaseController:
    @staticmethod
    def index():
        with Session as session:
            blog_items = session.query(BlogItem).all()

        return blog_items