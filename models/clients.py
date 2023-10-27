from pydantic import BaseModel
from typing import List, Optional

from models.addresses import AddressesModel

class ClientsModels(BaseModel):
    id: str
    firstName: str
    lastName: str
    birthDate: str
    preferredLanguage: str
    mobilePhone: str
    # rfc: str
    # curp: str
    emailAddress: Optional[str] = None
    addresses: List[AddressesModel]
    loanCycle: int
    groupLoanCycle: int
    clientRoleKey: str