from .. import db

class Blog(db.Model):
    __tablename__ = 'blogs'

    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.VARCHAR(100))
    summary=db.Column(db.VARCHAR(255))
    description=db.Column(db.Text)
    # New column
    created_at=db.Column(db.DateTime(timezone=True))
    updated_at=db.Column(db.DateTime(timezone=True))

    def __repr__(self) -> str:
        return f"Title={self.title}, ID={self.id}"