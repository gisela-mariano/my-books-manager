from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from src.core.utils.auth.auth_handler import decode_access_token
from src.core.utils.exceptions.errors import AuthUnauthorizedError


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        try:
            credentials: HTTPAuthorizationCredentials = await super(
                JWTBearer, self
            ).__call__(request)
        except HTTPException as e:
            raise AuthUnauthorizedError("Invalid authentication", metadata=[str(e)])

        if credentials:
            if not credentials.scheme == "Bearer":
                raise AuthUnauthorizedError("Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise AuthUnauthorizedError("Invalid or expired token.")
            return credentials.credentials
        else:
            raise AuthUnauthorizedError("Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        try:
            payload = decode_access_token(jwtoken)
        except:
            payload = None
        return bool(payload)
