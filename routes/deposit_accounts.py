import json
import requests
from pydantic import ValidationError
from models.onboarding import OnBoardingModel
from models.deposit_accounts import DepositAccountsModels
from config.config import URL_BASE, HEADERS

def create_deposit_account(onboarding: OnBoardingModel, account_holder_key: str, client_id: str):
    try:
        id_account = onboarding.rs_numerocuenta
        deposit_account_model = DepositAccountsModels(
            id=id_account,
            name="N2_" + id_account.replace("AP", "N"),
            accountHolderKey=account_holder_key
        )
        data = json.loads(deposit_account_model.model_dump_json())
        data["_CBE_INTER"] = {
            "_CBE_IN": "0000000000000000000"
        }
        response = requests.post(
            url=URL_BASE + "/api/deposits", json=data, headers=HEADERS, verify=False
        )
        result = response.json()
        if "id" in result:
            return {
                "code": "000", 
                "status": "successes", 
                "clientId": client_id,
                "accountHolderKey": account_holder_key,
                "accountEncodedKey": result["encodedKey"],
                "accountId": result["id"]
                }
        else:
            return {
                "code": "002",
                "status": result["errors"][0]["errorReason"],
                "clientId": "0000000000",
            }
    except ValidationError as e:
        return {"error": "Error de validación"}

def patch_deposit_account(onboarding: OnBoardingModel, clabe_account: str, client_id: str):
    try:
        id_account = onboarding.rs_numerocuenta
        data = [
            {
                "op": "REPLACE",
                "path": "_CBE_INTER",
                "value": {
                    "_CBE_IN": "0000000000000000001"
                }
            }
        ]
        data[0]["value"]["_CBE_IN"] = clabe_account
        response = requests.patch(
            url=URL_BASE + "/api/deposits/" + id_account, 
            json=data, 
            headers=HEADERS, 
            verify=False
        )
        
        if response.status_code == 204:
            return {
                "code": "000", 
                "status": "successes", 
                "clientId": client_id,
                }
        else:
            result = response.json()
            return {
                "code": "004",
                "status": result["errors"][0]["errorReason"],
                "clientId": "0000000000",
            }
    except ValidationError as e:
        return {"error": "Error de validación"}
    
def approve_deposit_account(onboarding: OnBoardingModel, client_id: str):
    try:
        id_account = onboarding.rs_numerocuenta
        data = {
            "action": "APPROVE",
            "notes": "Aprueba cuenta"
        }
        response = requests.post(
            url=URL_BASE + "/api/deposits/" + id_account + ":changeState", 
            json=data, 
            headers=HEADERS, 
            verify=False
        )
        
        result = response.json()
        
        if "id" in result:
            return {
                "code": "000", 
                "status": "successes", 
                "clientId": client_id,
                }
        else:
            return {
                "code": "005",
                "status": result["errors"][0]["errorReason"],
                "clientId": "0000000000",
            }
    except ValidationError as e:
        return {"error": "Error de validación"}