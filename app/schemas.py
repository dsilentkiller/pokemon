from typing import Optional
from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field

from pydantic.generics import GenericModel
T = TypeVar('T')


class PokemonSearchSchema(BaseModel):
    q: Optional[str] = None  # Search query for name match


class PokemonSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None
    image_path: Optional[str] = None

    class Config:
        orm_mode = True


class RequestPokemon(BaseModel):
    parameter: PokemonSchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
