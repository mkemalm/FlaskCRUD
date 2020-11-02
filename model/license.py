
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class License(db.Model):
    __tablename__ = 'license'
    license_label = db.Column(db.Integer, primary_key=True)
    license_model = db.Column(db.String(30), unique=False, nullable=True)
    license_count = db.Column(db.Numeric, unique=False, nullable=True)
    license_price = db.Column(db.Numeric, unique=False, nullable=True)
    license_currency = db.Column(db.String(10), unique=False, nullable=True)
    license_contract_number = db.Column(db.String(10), unique=False, nullable=True)
    license_start = db.Column(db.Date, unique=False, nullable=True)
    license_end = db.Column(db.Date, unique=False, nullable=True)

    def __init__(self, license_label, license_price, license_model, license_currency, license_count, license_contract_number, license_start, license_end):
        self.license_label = license_label
        self.license_model = license_model
        self.license_count = license_count
        self.license_price = license_price
        self.license_currency = license_currency
        self.license_contract_number = license_contract_number
        self.license_start = license_start
        self.license_end = license_end

    def __repr__(self):
        return f"<hardware {self.name}>"