from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField

class AddLicForm(FlaskForm):
    liclabel = StringField("Label")
    licname = StringField("License Name")
    licprice = StringField("Unit Price")
    curchoices = [('TRY','TRY'),('USD','USD'),('EUR','EUR')]
    liccurrency = SelectField("Currency", choices=curchoices)
    liccount = StringField("License Count")
    basechoices = [('CPUCore','CPU Core'),('CPUSocket','CPU Socket'),('Client','Client'),('Node','Node')]
    licmodel = SelectField("License Model", choices=basechoices)
    licstart = DateField("License Start",format="%m/%d/%Y")
    licend = DateField("License End",format="%m/%d/%Y")
    liccrno = StringField("Contract Number")
    licvendor = StringField("Vendor")
    licsupplier = StringField("Supplier")
    submitlic = SubmitField("Add License")