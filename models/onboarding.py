from pydantic import BaseModel
from typing import Optional

class OnBoardingModel(BaseModel):
        firstname: str
        middlename: str
        lastname: str
        rs_fechanacimiento: str
        mobilephone: str
        rs_rfc: str
        rs_curp: str
        emailaddress1: str
        address1_line1: str
        address1_line2: str
        address1_line3: Optional[str] = None
        address1_postalcode: str
        rs_municipio: str
        rs_colonia: str
        rs_numerocuenta: str
        rs_numerocliente: str
        