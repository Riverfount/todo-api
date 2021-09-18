from typing import Optional

from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

# from api.config import settings


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(request, credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    # noinspection PyBroadException
    @staticmethod
    def verify_jwt(request: Request, token: Optional) -> bool:
        is_token_valid: bool = False
        auth_jwt = AuthJWT(request, token)
        try:
            payload = auth_jwt.get_raw_jwt()
        except Exception:
            payload = None
        if payload:
            is_token_valid = True
        return is_token_valid


class Settings(BaseModel):
    # authjwt_secret_key: str = settings.JWT_SECRET
    authjwt_secret_key: str = "AquiVemAMinhaSuperHyperTopSecretKey"


# callback to get your configuration
@AuthJWT.load_config
def get_config():
    return Settings()
