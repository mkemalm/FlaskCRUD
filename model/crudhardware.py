from model.hardware import Hardware
from flask_sqlalchemy import SQLAlchemy
from views.addhw import AddHwForm
from views.search import SearchForm

class CrudHardware:
    @staticmethod
    def saveHardware(addhwForm=AddHwForm, db=SQLAlchemy):
        serialno = addhwForm.serialno.data
        hwlabel = addhwForm.hwlabel.data
        hwmodel = addhwForm.hwmodel.data
        hwtype = addhwForm.hwtype.data
        hwprice = addhwForm.price.data
        hwcurrency = addhwForm.currency.data
        warrantystart = addhwForm.warrantystart.data
        warrantyend = addhwForm.warrantyend.data
        hwvendor = addhwForm.hwvendor.data
        hwsupplier = addhwForm.hwsupplier.data   
        hwcrno = addhwForm.hwcrno.data
        hw_e = Hardware.query.filter_by(serial_number=serialno).first()
        if hw_e is None:
            hw = Hardware(serial_number=serialno, hardware_label=hwlabel, hardware_model=hwmodel, hardware_type=hwtype,price=hwprice, currency=hwcurrency, contract_number=hwcrno, warranty_start=warrantystart, warranty_end=warrantyend,vendor=hwvendor,supplier=hwsupplier)
            db.session.add(hw)
            db.session.commit()
            return 1
        return 0
 
    @staticmethod
    def searchHardware(searchForm=SearchForm, db=SQLAlchemy):
        searchlabel = searchForm.searchlabel.data
        searchvendor = searchForm.searchvendor.data
        searchsupplier = searchForm.searchsupplier.data
        searchtype = searchForm.searchtype.data
        print(searchtype)
        print(searchlabel)
        if searchtype == "Hardware":
            result = Hardware.query.filter(Hardware.hardware_label.startswith(searchlabel)).all()
            return result
            #print(result[0].serial_number)
            
           


