from routes.router import api_router
from fastapi import FastAPI

api = FastAPI(
    title="OnBoarding",
    description="API OnBoarding",
    version="1.0.0"
)
api.include_router(api_router)

# api.redoc_url = None
# api.swagger_ui_oauth2_redirect_url = None
