from pydantic import BaseModel

class ClabeAccounts(BaseModel):
    cuenta: str
    producto: str = "6150"
    sucursal: str = "0062"
    sistema: str = "MB"