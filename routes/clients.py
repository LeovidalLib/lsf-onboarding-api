import json
import requests
from pydantic import ValidationError
from models.onboarding import OnBoardingModel
from models.clients import ClientsModels
from models.addresses import AddressesModel
from config.config import URL_BASE, HEADERS
from utils.generators import GeneratorsUtils
# from fastapi import APIRouter

# clients_router = APIRouter()
# @clients_router.post("/clients")
def create_clients(onboarding: OnBoardingModel):
    try:
        # onboarding_data = onboarding.model_dump()
        generators = GeneratorsUtils()
        # client_id = onboarding.rs_numerocliente
        # client_id = client_id if client_id is not None else generators.id_client_generator()
        client_id = generators.id_client_generator()
        clients_model = ClientsModels(
            id=client_id,
            firstName=onboarding.firstname,
            middleName=onboarding.middlename,
            lastName=onboarding.lastname,
            homePhone=onboarding.telephone1,
            mobilePhone=onboarding.mobilephone,
            emailAddress=onboarding.emailaddress1,
            preferredLanguage="SPANISH",
            birthDate=onboarding.rs_fechanacimiento,
            gender=onboarding.rs_genero,
            addresses=[
                AddressesModel(
                    line1=onboarding.address1_line1,
                    line2=onboarding.address1_line2,
                    city=onboarding.rs_municipio,
                    region=onboarding.rs_municipio,
                    postcode=onboarding.address1_postalcode,
                    country="Mexico",
                )
            ],
            loanCycle=0,
            groupLoanCycle=0,
            clientRoleKey="8ac9821e8af48ceb018afbbc778700e0",
            assignedBranchKey="8ac9827d8ad0f770018adde687ae00ec"
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
