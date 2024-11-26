from app import db 
from datetime import datetime

class Data(db.Model):
    id   = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=False)
    distance_x_cm = db.Column(db.String(60), index=True, unique=True, nullable=False)
    distance_y_cm = db.Column(db.String(100), nullable=False)
    goods_received_kg= db.Column(db.String(100), nullable=False)
    estimated_time= db.Column(db.String(100), nullable=False)
    lead_time= db.Column(db.String(100), nullable=False)
