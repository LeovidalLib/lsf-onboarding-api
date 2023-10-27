from dotenv import dotenv_values

values = dotenv_values(".env_dev")

URL_BASE = values["URL_BASE"]
CLIENT_ID_NAME = values["CLIENT_ID_NAME"]
CLIENT_ID_SECRET = values["CLIENT_ID_SECRET"]
CLIENT_SECRET_NAME = values["CLIENT_SECRET_NAME"]
CLIENT_SECRET_ID = values["CLIENT_SECRET_ID"]
ACCEPT_MAMBU_V2 = values["ACCEPT_MAMBU_V2"]

HEADERS={
    "Content-Type": "application/json",
    CLIENT_ID_NAME: CLIENT_ID_SECRET,
    CLIENT_SECRET_NAME: CLIENT_SECRET_ID,
    "Accept": ACCEPT_MAMBU_V2
}