from flask import Flask,render_template,redirect,request,url_for
from models.hardware import Hardware
from flask_sqlalchemy import SQLAlchemy
from views.addhw import AddHwForm 
from views.addlic import AddLicForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'

# Configure database
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://invmgmt:inv2020@127.0.0.1/invdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/addhw',methods=['GET','POST'])
def addhw():
    addhwForm = AddHwForm()

    if addhwForm.validate_on_submit and request.method == 'POST':
        serialno = addhwForm.serialno.data
        hwlabel = addhwForm.hwlabel.data
        hwmodel =  addhwForm.hwmodel.data
        hwtype = addhwForm.hwtype.data
        hwprice = addhwForm.price.data
        hwcurrency = addhwForm.currency.data
        warrantystart = addhwForm.warrantystart.data
        warrantyend = addhwForm.warrantyend.data
        hwcrno = addhwForm.hwcrno.data
        hw_e = Hardware.query.filter_by(serial_number=serialno).first()
        if hw_e is None:
            hw = Hardware(serial_number=serialno, hardware_label=hwlabel, hardware_model=hwmodel, hardware_type=hwtype,price=hwprice,currency=hwcurrency,contract_number=hwcrno,warranty_start=warrantystart,warranty_end=warrantyend)
            db.session.add(hw)
            db.session.commit()
            return render_template('addhw.html', form=addhwForm, msg='Hardware added.')
        else: 
            return render_template('addhw.html', form=addhwForm, msg='Hardware exists.')
    else:
        return render_template('addhw.html', form=addhwForm, msg=' ')

@app.route('/addlic',methods=['GET','POST'])
def addlic():
    addlicForm = AddLicForm()
    return render_template('addlic.html', form=addlicForm)

if __name__ == '__main__':
    app.run(debug=True)