
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Hardware(db.Model):
    __tablename__ = 'hardware'
    hardware_id = db.Column(db.Integer, primary_key=True)
    serial_number = db.Column(db.String(50), unique=True, nullable=False)
    hardware_label = db.Column(db.String(50), unique=False, nullable=False)
    hardware_model = db.Column(db.String(50), unique=False, nullable=True)
    hardware_type = db.Column(db.String(50), unique=False, nullable=True)
    price = db.Column(db.Numeric, unique=False, nullable=True)
    currency = db.Column(db.String(10), unique=False, nullable=True)
    contract_number = db.Column(db.String(10), unique=False, nullable=True)
    warranty_start = db.Column(db.Date, unique=False, nullable=True)
    warranty_end = db.Column(db.Date, unique=False, nullable=True)

    def __init__(self, serial_number, hardware_label, hardware_model,hardware_type,price,currency,contract_number,warranty_start,warranty_end):
        self.serial_number = serial_number
        self.hardware_label = hardware_label
        self.hardware_model = hardware_model
        self.hardware_type = hardware_type
        self.price = price
        self.currency = currency
        self.contract_number = contract_number
        self.warranty_start = warranty_start
        self.warranty_end = warranty_end

    def __repr__(self):
        return f"<hardware {self.name}>"