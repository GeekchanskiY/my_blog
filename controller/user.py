from db import Session
import hashlib
from model.models import User

class UserController:
    @staticmethod
    def register(username, password, repeat_password):
        if password != repeat_password:
            raise ValueError("Passwords do not match")

        with Session as session:
            existing_user = session.query(User).filter_by(name=username).first()
            if existing_user:
                raise ValueError("Username already taken")

            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            new_user = User(name=username, password=hashed_password)

            session.add(new_user)

            session.commit()

            session.refresh(new_user)
        
        return new_user