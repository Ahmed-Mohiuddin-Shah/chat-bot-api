from fastapi import FastAPI, Body, Depends, APIRouter
from starlette.middleware.cors import CORSMiddleware
from decouple import config

from app.auth.fastapi_auth_middlewares import JwtAuthMiddleware

from app.utils.custom_cors_middleware import CustomCORSMiddleware

from app.routes.auth_router import router as auth_router

api_router = APIRouter()

def get_application() -> FastAPI:
    application = FastAPI(title=config("API_TITLE"), debug=True)
    application.include_router(api_router, prefix="")

    # application.add_middleware(CustomCORSMiddleware)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(auth_router, prefix="/api/auth", tags=["auth"])

    # application.add_middleware(
    #     JwtAuthMiddleware,
    #     secret_key=config("SALT"),
    #     algorithms=[config("JWT_ALGORITHM"),],
    #     public_paths=["/docs", "/openapi.json", "/api/auth", "/api/websockets", "/api/rtsp-streams"],
    # )
    
    return application


app = get_application()
