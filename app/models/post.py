from .db import db
from .tagged_images import tagged_images
from sqlalchemy.sql import func

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    postImageUrl = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(50))
    createdAt = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    updatedAt = db.Column(db.DateTime(timezone=True), server_onupdate=func.now(), server_default=func.now())

    user = db.relationship('User', back_populates='posts')
    comments = db.relationship('Comment', back_populates='post', cascade="all, delete")
    tags = db.relationship('Tag', secondary=tagged_images, back_populates='posts')

    def to_dict_lite(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'postImageUrl': self.postImageUrl,
            'title': self.title,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt,
            'user': self.user.to_dict()
        }


    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'postImageUrl': self.postImageUrl,
            'title': self.title,
            'comments': [comment.to_dict() for comment in self.comments],
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt,
            'user': self.user.to_dict(),
            'tags': [tag.to_dict_lite() for tag in self.tags]
        }
