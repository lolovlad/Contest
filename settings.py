from pydantic import BaseSettings
from typing import List


class Settings(BaseSettings):
    mode: str
    path_browser: str
    args: str
    port_app: int = 8000
    start_file: str
    host_server: str
    port_server: int
    token: str
    host_server_socket: str
    port_server_socket: int


settings = Settings(_env_file="Files/settings_app.env", _env_file_encoding="utf-8")