from extensions.database import db

class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    parameter = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Parameter model: {self.parameter}, created at {self.date_created}"
