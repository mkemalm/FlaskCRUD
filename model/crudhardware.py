from model.hardware import Hardware
from flask_sqlalchemy import SQLAlchemy
from views.addhw import AddHwForm

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
        hwcrno = addhwForm.hwcrno.data
        hw_e = Hardware.query.filter_by(serial_number=serialno).first()
        if hw_e is None:
            hw = Hardware(serial_number=serialno, hardware_label=hwlabel, hardware_model=hwmodel, hardware_type=hwtype,price=hwprice, currency=hwcurrency, contract_number=hwcrno, warranty_start=warrantystart, warranty_end=warrantyend)
            db.session.add(hw)
            db.session.commit()
            return 1
        return 0
