from flask import Flask,render_template,redirect,request
from view.addhw import AddHwForm 
from view.addlic import AddLicForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/addhw',methods=['GET','POST'])
def addhw():
    addhwForm = AddHwForm()
    return render_template('addhw.html', form=addhwForm)

@app.route('/addlic',methods=['GET','POST'])
def addlic():
    addlicForm = AddLicForm()
    return render_template('addlic.html', form=addlicForm)

if __name__ == '__main__':
    app.run()