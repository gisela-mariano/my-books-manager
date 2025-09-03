from passlib.context import CryptContext
from src.core.components.v1.auth.infra.schemas.auth import Token, TokenData
from src.core.components.v1.users.domain.user_repository import UserRepository
from src.core.utils.auth.auth_handler import create_access_token, decode_access_token
from src.core.utils.exceptions.errors import AuthUnauthorizedError, CredentialError


class AuthService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    _pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def authenticate_user(self, email: str, password: str):
        user = await self.user_repository.get_by_email(email)

        if not user:
            raise AuthUnauthorizedError()

        if not self._verify_password(password, user.get("hashed_password")):
            raise AuthUnauthorizedError()

        token_data = TokenData(**user).model_dump(by_alias=True)

        access_token = create_access_token(data={"sub": {**token_data}})

        return Token(access_token=access_token, token_type="bearer").model_dump(
            by_alias=True
        )

    async def get_current_user(self, token: str):
        user_data = decode_access_token(token)

        user = await self.user_repository.get_by_email(user_data.get("email"))

        if not user:
            raise CredentialError("Could not validate credentials")

        return user

    def get_password_hash(self, password):
        return self._pwd_context.hash(password)

    def _verify_password(self, plain_password, hashed_password):
        return self._pwd_context.verify(plain_password, hashed_password)
