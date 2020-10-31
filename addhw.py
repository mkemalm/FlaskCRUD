from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField

class AddHwForm(FlaskForm):
    serialno = StringField("Serial Number")
    hwmodel = StringField("Model")
    hwtype = StringField("Type")
    hwlabel = StringField("Label")
    price = StringField("Price")
    curchoices = [('TRY','TRY'),('USD','USD'),('EUR','EUR')]
    currency = SelectField("Currency", choices=curchoices)
    warrantystart = DateField("Warranty Start")
    warrantyend = DateField("Warranty End")
    hwcrno = StringField("Contract Number")
    submithw = SubmitField("Add Hardware")