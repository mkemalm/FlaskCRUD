from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

class SearchForm(FlaskForm):
    searchlabel = StringField("Label")
    searchvendor = StringField("Vendor")
    searchsupplier = StringField("Label")
    invtypes = [('License','License'),('Hardware','Hardware')]
    searchtype = SelectField("Type", choices=invtypes)
    searchsubmit = SubmitField("Search")