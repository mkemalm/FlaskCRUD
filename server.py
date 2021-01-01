from flask import Flask,render_template,redirect,request,url_for
from model.hardware import Hardware
from flask_sqlalchemy import SQLAlchemy
from views.addhw import AddHwForm 
from views.addlic import AddLicForm
from views.search import SearchForm
from model.crudhardware import CrudHardware
from model.crudlicense import CrudLicense

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
        rtrnhw = CrudHardware.saveHardware(addhwForm, db)
        if rtrnhw > 0:
            return render_template('addhw.html', form=addhwForm, msg='Hardware added.')
        return render_template('addhw.html', form=addhwForm, msg='Hardware exists.')
    else:
        return render_template('addhw.html', form=addhwForm, msg=' ')

@app.route('/addlic',methods=['GET','POST'])
def addlic():
    addlicForm = AddLicForm()
    if addlicForm.validate_on_submit and request.method == 'POST':
        rtrnlic = CrudLicense.saveLicense(addlicForm, db)
        if rtrnlic > 0:
            return render_template('addlic.html', form=addlicForm, msg='License added.')
        return render_template('addlic.html', form=addlicForm, msg='License exists.')
    else:
        return render_template('addlic.html', form=addlicForm, msg=' ')

@app.route('/search',methods=['GET','POST'])
def search():
    searchForm = SearchForm()
    if searchForm.validate_on_submit and request.method == 'POST':
        search_type = request.form.get("searchtype")
        if  search_type == "Hardware":
            hwresult = CrudHardware.searchHardware(searchForm, db)
            print(len(hwresult))
            print(hwresult[0].serial_number)
            return render_template('search.html',form=searchForm, msg=' ', results=hwresult)
    return render_template('search.html',form=searchForm, msg=' ')

if __name__ == '__main__':
    app.run(debug=True)