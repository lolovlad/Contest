from pydantic import BaseModel


class Login(BaseModel):
    login: str = None
    password: str = None
