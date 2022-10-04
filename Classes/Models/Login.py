from pydantic import BaseModel


class Token(BaseModel):
    access_token: str = ""
    token_type: str = 'bearer'
    type_user: int = 0


class Login(BaseModel):
    login: str = None
    password: str = None
