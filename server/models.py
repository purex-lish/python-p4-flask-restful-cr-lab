from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Numeric, String

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=True)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    
    def __init__(self, name, image=None, price=0.0):  # Set default price
        self.name = name
        self.image = image
        self.price = price
        
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'price': float(self.price)  # Convert Decimal to float
        }