from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, int, enum
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "User"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    lastname: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
        }

class Followers(db.Model):
    __tablename__ = "Follower"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_from_id: Mapped[int] = mapped_column(ForeignKey("user.id") primary_key=True)
    user_to_id: Mapped[int] = mapped_column(ForeignKey("user.id") primary_key=True)

    def serialize(self):
        return {
            "id": self.id,
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id,
        }
    
class Comments(db.Model):
    __tablename__ = "Comment"
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(120), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id") primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("user.id") primary_key=True)

    def serialize(self):
        return {
            "id": self.id,
            "comment_text": self.comment_text,
            "email": self.email,
            "author_id": self.author_id,
            "post_id": self.post_id,
        }
    
class Posts(db.Model):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped["Medias"] = relationship(back_populates="post")

    user_id: Mapped[int] = mapped_coluFmn(oreignKey("users.id"))
    user: Mapped["Users"] = relationship(back_populates="post")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
        }
    
class Medias(db.Model):
    __tablename__ = "medias"
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(ForeignKey("Posts.id"))
    url: Mapped[str] = relationship(back_populates="Medi")
    post_id: Mapped[int] = mapped_column(ForeignKey("Posts.id") primary_key=True)

    profile: Mapped["Profiles"] = relationship(back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "email": self.email,
            "url": self.url,
            "post_id": self.post_id,
        }
