from db import Session
from model.models import BlogItem
from datetime import datetime

class BlogController:
    @staticmethod
    def blog_post(post_id):
        with Session as session:
            blog_item = session.query(BlogItem).where(BlogItem.id == post_id).first()
        
        if not blog_item:
            raise ValueError("Post not found")

        return blog_item
    
    @staticmethod
    def add_post(title, content):
        if not title or not content:
            raise ValueError("Title and content cannot be empty")
        
        with Session as session:
            new_post = BlogItem(title=title, content=content, created_at=datetime.now(), updated_at=datetime.now())

            session.add(new_post)

            session.commit()

            session.refresh(new_post)
        
        return new_post.id
    
    @staticmethod
    def delete_post(post_id):
        with Session as session:
            post = session.query(BlogItem).filter(BlogItem.id == post_id).first()
            
            if post:
                session.delete(post)
                session.commit()

                return True
        
        return False