# generated by datamodel-codegen:
#   filename:  nested_json_pointer.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Optional, Union

from pydantic import BaseModel, Extra, Field


class CatBreed(BaseModel):
    __root__: Any


class DogBreed(BaseModel):
    __root__: Any


class Pets(BaseModel):
    __root__: Any


class PetType(Enum):
    Cat = 'Cat'


class PetType1(Enum):
    Dog = 'Dog'


class C1(BaseModel):
    hunts: Optional[bool] = None
    age: Optional[str] = None


class C2(BaseModel):
    hunts: Optional[bool] = None
    age: Optional[str] = None


class D1(BaseModel):
    bark: Optional[bool] = None
    age: Optional[str] = None


class D2(BaseModel):
    hunts: Optional[bool] = None
    age: Optional[str] = None


class Cat(BaseModel):
    pet_type: PetType
    breed: Optional[Union[C1, C2]] = Field(None, title='breed')


class Dog(BaseModel):
    pet_type: PetType1
    breed: Union[D1, D2] = Field(..., title='breed')


class Person(BaseModel):
    class Config:
        extra = Extra.forbid

    name: Optional[str] = Field(None, title='name')
    pet: Optional[Union[Cat, Dog]] = Field(None, title='pet')
