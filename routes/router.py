from fastapi import APIRouter
from routes.onboarding import onboarding_router
# from routes.clients import clients_router

api_router = APIRouter()
api_router.include_router(onboarding_router, prefix="")
# api_router.include_router(clients_router, prefix="")