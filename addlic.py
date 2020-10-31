from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField

class AddLicForm(FlaskForm):
    liclabel = StringField("Label")
    licprice = StringField("Unit Price")
    curchoices = [('TRY','TRY'),('USD','USD'),('EUR','EUR')]
    liccurrency = SelectField("Currency", choices=curchoices)
    licnumber = StringField("License Number")
    basechoices = [('CPUCore','CPU Core'),('CPUSocket','CPU Socket'),('Client','Client'),('Node','Node')]
    licmodel = SelectField("License Model", choices=basechoices)
    licstart = DateField("License Start")
    licend = DateField("License End")
    liccrno = StringField("Contract Number")
    submitlic = SubmitField("Add License")