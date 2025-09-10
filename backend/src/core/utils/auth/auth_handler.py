import os
from datetime import datetime, timedelta, timezone

import jwt
from jwt.exceptions import InvalidTokenError
from src.core.components.v1.auth.infra.schemas.auth import TokenUserData
from src.core.utils.exceptions.errors import CredentialError

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict[TokenUserData]) -> str:
    to_encode = {"user": data.copy()}

    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "iat": datetime.now(timezone.utc)})

    encoded_jwt = jwt.encode(payload=to_encode, key=SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def decode_access_token(token: str) -> dict:
    try:
        result = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        return result
    except InvalidTokenError as e:
        raise CredentialError("Invalid token", metadata=[str(e)])
    except Exception as e:
        raise CredentialError("Could not validate credentials", metadata=[str(e)])
