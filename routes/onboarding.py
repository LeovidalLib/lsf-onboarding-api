from fastapi import APIRouter
from pydantic import ValidationError
from models.onboarding import OnBoardingModel
from routes.clients import create_clients
from routes.deposit_accounts import create_deposit_account, patch_deposit_account, approve_deposit_account
from routes.clabe_accounts import create_clabe_accounts
from routes.contracts import create_contracts

onboarding_router = APIRouter()

@onboarding_router.post("/onboarding")
async def root(onboarding: OnBoardingModel):
    try:
        clients_response = create_clients(onboarding=onboarding)
        if "code" in clients_response:
            if clients_response.get("code") == "000":
                client_encoded_key = clients_response.get("clientEncodedKey")
                id_client = clients_response.get("clientId")
                deposit_response = create_deposit_account(
                    account_holder_key=client_encoded_key, 
                    client_id=id_client
                )
                if deposit_response.get("code") == "000":
                    account_id = deposit_response.get("accountId")
                    creation_date_deposit_account = deposit_response.get("creationDate")
                    clabe_response = create_clabe_accounts(
                        account_id=account_id, 
                        client_id=id_client)
                    if clabe_response.get("code") == "000":
                        clabe_account = clabe_response.get("ctaClabe")
                        patch_account = patch_deposit_account(
                            # onboarding=onboarding,
                            account_id=account_id,
                            clabe_account=clabe_account,
                            client_id=id_client
                        )
                        if patch_account.get("code") == "000":
                            contracts_data = {
                                "id_account": account_id,
                                "id_client": id_client,
                                "clabe": clabe_account,
                                "account_creation": creation_date_deposit_account
                            }
                            
                            contracts_account = create_contracts(
                                onboarding=onboarding,
                                data_contract=contracts_data
                            )
                            if contracts_account.get("code") == "000":
                                approve_account = approve_deposit_account(
                                    account_id=account_id,
                                    client_id=id_client
                                )
                                if approve_account.get("code") == "000":
                                    return approve_account
                                else:
                                    return approve_account
                            else:
                                return define_response(contracts_account)
                        else:
                            return define_response(patch_account)
                    else:
                        return define_response(clabe_response)
                else:
                    return define_response(deposit_response)
            else:
                return define_response(clients_response)
            
    except ValidationError as e:
        return {"error": "Error de validación"}
    
def define_response(response):
    try:
        code = response.get("code")
        status = response.get("status")
        client_id = response.get("clientId")
        return {
            "code": code,
            "status": status,
            "clientId": client_id
        }
    except Exception as httpexc:
        print(httpexc)