import json
import requests
from pydantic import ValidationError
from models.onboarding import OnBoardingModel
from models.clients import ClientsModels
from models.addresses import AddressesModel
from config.config import URL_BASE, HEADERS

# from fastapi import APIRouter
from pydantic import ValidationError
from models.clients import ClientsModels

# clients_router = APIRouter()
# @clients_router.post("/clients")
def create_clients(onboarding: OnBoardingModel):
    try:
        # onboarding_data = onboarding.model_dump()
        clients_model = ClientsModels(
            id=onboarding.rs_numerocliente,
            firstName=onboarding.firstname,
            lastName=onboarding.lastname,
            birthDate=onboarding.rs_fechanacimiento,
            preferredLanguage="SPANISH",
            mobilePhone=onboarding.mobilephone,
            emailAddress=onboarding.emailaddress1,
            addresses=[
                AddressesModel(
                    line1=onboarding.address1_line1,
                    line2=onboarding.address1_line2,
                    postcode=onboarding.address1_postalcode,
                    region=onboarding.rs_municipio,
                    city=onboarding.rs_municipio,
                    country="Mexico",
                )
            ],
            loanCycle=0,
            groupLoanCycle=0,
            clientRoleKey="8ac9821e8af48ceb018afbbc778700e0",
        )
        data = json.loads(clients_model.model_dump_json())
        data["_Clientes_N2"] = {
            "_CURP": onboarding.rs_curp,
            "_RFC": onboarding.rs_rfc
        }
        response = requests.post(
            url=URL_BASE + "/api/clients", json=data, headers=HEADERS, verify=False
        )
        result = response.json()
        if "id" in result:
            return {
                "code": "000", 
                "status": "successes", 
                "clientId": result["id"],
                "clientEncodedKey": result["encodedKey"]
                }
        else:
            return {
                "code": "001",
                "status": result["errors"][0]["errorReason"],
                "clientId": "0000000000",
            }
    except ValidationError as e:
        return {"error": "Error de validación"}
