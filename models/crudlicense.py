from models.license import License
from flask_sqlalchemy import SQLAlchemy
from views.addlic import AddLicForm

class CrudLicense:
    @staticmethod
    def saveLicense(addlicForm=AddLicForm, db=SQLAlchemy):
        liclabel = addlicForm.liclabel.data
        licprice = addlicForm.licprice.data
        licmodel = addlicForm.licmodel.data
        liccurrency = addlicForm.liccurrency.data
        liccount = addlicForm.liccount.data
        liccrno = addlicForm.liccrno.data
        licstart = addlicForm.licstart.data
        licend = addlicForm.licend.data
        hw_l = License.query.filter_by(license_label=liclabel).first()
        if hw_l is None:
            print(licstart)
            print(licend)
            lic = License(license_label=liclabel, license_price=licprice, license_model=licmodel, license_currency=liccurrency, license_count=liccount, license_contract_number=liccurrency, license_start=licstart, license_end=licend)
            db.session.add(lic)
            db.session.commit()
            return 1
        return 0
        db.session.add(lic)
        db.session.commit()
        
