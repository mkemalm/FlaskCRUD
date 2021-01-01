from model.license import License
from flask_sqlalchemy import SQLAlchemy
from views.addlic import AddLicForm

class CrudLicense:
    @staticmethod
    def saveLicense(addlicForm=AddLicForm, db=SQLAlchemy):
        liclabel = addlicForm.liclabel.data
        licname = addlicForm.licname.data
        licprice = addlicForm.licprice.data
        licmodel = addlicForm.licmodel.data
        liccurrency = addlicForm.liccurrency.data
        liccount = addlicForm.liccount.data
        liccrno = addlicForm.liccrno.data
        licstart = addlicForm.licstart.data
        licend = addlicForm.licend.data
        licvendor = addlicForm.licvendor.data
        licsupplier = addlicForm.licsupplier.data
        lic_e = License.query.filter_by(license_label=liclabel).first()
        if lic_e is None:
            print(licstart)
            print(licend)
            lic = License(license_label=liclabel, license_name=licname,license_price=licprice, license_model=licmodel, license_currency=liccurrency, license_count=liccount, license_contract_number=liccurrency, license_start=licstart, license_end=licend,vendor=licvendor,supplier=licsupplier)
            db.session.add(lic)
            db.session.commit()
            return 1
        return 0
        db.session.add(lic)
        db.session.commit()
        
