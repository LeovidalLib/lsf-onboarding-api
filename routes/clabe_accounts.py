import json
import requests
from pydantic import ValidationError
from models.clabe_accounts import ClabeAccounts
from config.config import URL_BASE, HEADERS

def create_clabe_accounts(account_id: str, client_id: str):
    try:
        clabe_model = ClabeAccounts(
            cuenta=account_id
        )
        data = json.loads(clabe_model.model_dump_json())
        response = requests.post(
            url=URL_BASE + "/lsfcoresif/v1/generactacb", json=data, headers=HEADERS, verify=False
        )
        result = response.json()
        if "code" in result:
            return {
                "code": "000", 
                "status": "successes", 
                "clientId": client_id,
                "ctaClabe": result["ctaClabe"]
                }
        else:
            return {
                "code": "003",
                "status": "No CTA CLABE",
                "clientId": "000",
            }
    except ValidationError as e:
        return {"error": "Error de validación"}
