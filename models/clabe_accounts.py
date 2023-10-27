from pydantic import BaseModel

class ClabeAccounts(BaseModel):
    cuenta: str
    producto: str = "9989"
    sucursal: str = "99"
    sistema: str = "99"