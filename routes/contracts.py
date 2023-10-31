import json
import requests
from pydantic import ValidationError
from models.onboarding import OnBoardingModel
from models.contracts import ContractsModels
from config.config import URL_BASE, HEADERS

def create_contracts(onboarding: OnBoardingModel, data_contract: dict):
    try:
        contracts_model = ContractsModels(
            firstname=onboarding.firstname,
            rs_segundonombre=onboarding.rs_segundonombre,
            middlename=onboarding.middlename,
            lastname=onboarding.lastname,
            rs_fechanacimiento=onboarding.rs_fechanacimiento,
            mobilephone=onboarding.mobilephone,
            rs_rfc=onboarding.rs_rfc,
            rs_curp=onboarding.rs_curp,
            emailaddress1=onboarding.emailaddress1,
            rs_genero=onboarding.rs_genero,
            rs_paisnacimiento=onboarding.rs_paisnacimiento,
            rs_lugarnacimiento=onboarding.rs_lugarnacimiento,
            rs_nacionalidad=onboarding.rs_nacionalidad,
            address1_line1=onboarding.address1_line1,
            address1_line2=onboarding.address1_line2,
            address1_line3=onboarding.address1_line3,
            address1_postalcode=onboarding.address1_postalcode,
            rs_entidadfederativa=onboarding.rs_entidadfederativa,
            rs_municipio=onboarding.rs_municipio,
            rs_colonia=onboarding.rs_colonia,
            interviewid=onboarding.interviewid,
            telephone1=onboarding.telephone1,
            rs_coloniaid=onboarding.rs_coloniaid,
            rs_numerocuenta=data_contract["id_account"],
            rs_numerocliente=data_contract["id_client"],
            rs_cuentaclabemambu=data_contract["clabe"],
            rs_clave="000",
            rs_fechaapertura=data_contract["account_creation"]
        )
        
        data = json.loads(contracts_model.model_dump_json())

        response = requests.post(
            url=URL_BASE + "/dynamics/v1/contratos", json=data, headers=HEADERS, verify=False
        )
        result = response.json()
        if result.get("code") == "000":
            return {
                "code": "000", 
                "status": "successes", 
                "clientId": data_contract["id_client"]
                }
        else:
            return {
                "code": "001",
                "status": result["errors"][0]["errorReason"],
                "clientId": "0000000000",
            }
    except ValidationError as e:
        return {
                "code": "001",
                "status": result["errors"][0]["errorReason"],
                "clientId": "0000000000",
            }
