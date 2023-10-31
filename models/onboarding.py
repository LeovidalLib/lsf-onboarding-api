from pydantic import BaseModel
from typing import Optional

class OnBoardingModel(BaseModel):
        # firstname: str
        # middlename: str
        # lastname: str
        # rs_fechanacimiento: str
        # mobilephone: str
        # rs_rfc: str
        # rs_curp: str
        # emailaddress1: str
        # address1_line1: str
        # address1_line2: str
        # address1_line3: Optional[str] = None
        # address1_postalcode: str
        # rs_municipio: str
        # rs_colonia: str
        # rs_numerocuenta: Optional[str] = None
        # rs_numerocliente: Optional[str] = None
        
        firstname: str
        rs_segundonombre: Optional[str] = None
        middlename: str
        lastname: str
        rs_fechanacimiento: str
        mobilephone: str
        rs_rfc: str
        rs_curp: str
        emailaddress1: str
        rs_genero: str
        rs_paisnacimiento: str
        rs_lugarnacimiento: str
        rs_nacionalidad: str
        address1_line1: str
        address1_line2: str
        address1_line3: Optional[str] = None
        address1_postalcode: str
        rs_entidadfederativa: str
        rs_municipio: str
        rs_colonia: str
        interviewid: str
        telephone1: str
        rs_coloniaid: str