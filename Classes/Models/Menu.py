from pydantic import BaseModel
from Classes.Models.Contest import ContestGet
from typing import List


class Menu(BaseModel):
    state_user: int = 0
    contests: ContestGet = ContestGet()
