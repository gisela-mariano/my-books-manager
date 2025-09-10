from typing import Optional

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

        if not credentials or credentials.scheme != "Bearer":
            raise AuthUnauthorizedError("Invalid authentication scheme.")

        payload = self.verify_jwt(credentials.credentials)

        if not payload:
            raise AuthUnauthorizedError("Invalid or expired token.")

        request.state.user = payload.get("user")

    def verify_jwt(self, jwtoken: str) -> Optional[dict]:
        try:
            return decode_access_token(jwtoken)
        except Exception:
            return None
