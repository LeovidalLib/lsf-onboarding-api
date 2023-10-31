from pydantic import BaseModel
from typing import List, Optional

from models.addresses import AddressesModel

class ClientsModels(BaseModel):
    id: str
    firstName: str
    middleName: str
    lastName: str
    homePhone: str
    mobilePhone: str
    emailAddress: Optional[str] = None
    preferredLanguage: str
    birthDate: str
    gender: str
    addresses: List[AddressesModel]
    loanCycle: int
    groupLoanCycle: int
    clientRoleKey: str
    assignedBranchKey: str
    # rfc: str
    # curp: str