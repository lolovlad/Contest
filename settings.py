from pydantic import BaseSettings


class Settings(BaseSettings):
    path_browser: str = "chrome"
    port_app: int = 8000
    start_file: str
    host_server: str
    port_server: int
    token: str


settings = Settings(_env_file="Files/settings_app.env", _env_file_encoding="utf-8")