from .. import db

class User(db.Model):
    __tablename__ = 'users'

    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(50))
    last_name=db.Column(db.String(50))

    def __repr__(self) -> str:
        return f"First name={self.first_name}, Last name={self.last_name}"