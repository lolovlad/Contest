from typing import List
from enum import Enum
from pydantic import BaseModel


class TypeOrganization(int, Enum):
    School = 1
    University = 2
    College = 3
    Other = 4


class Organization(BaseModel):
    id: int
    name_organizations: str
    type_organizations: TypeOrganization

