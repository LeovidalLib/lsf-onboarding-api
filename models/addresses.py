from pydantic import BaseModel

class AddressesModel(BaseModel):
        line1: str
        line2: str
        city: str
        region: str
        postcode: str
        country: str