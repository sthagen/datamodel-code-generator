# generated by datamodel-codegen:
#   filename:  discriminator_literals.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import Annotated, ClassVar, Literal, Optional, Union

from msgspec import Meta, Struct


class Type1(Struct, kw_only=True, tag_field='type_', tag='a'):
    type_: ClassVar[Annotated[Literal['a'], Meta(title='Type ')]] = 'a'


class Type2(Struct, kw_only=True, tag_field='type_', tag='b'):
    type_: ClassVar[Annotated[Literal['b'], Meta(title='Type ')]] = 'b'


class UnrelatedType(Struct, kw_only=True):
    info: Optional[Annotated[str, Meta(title='A way to check for side effects')]] = (
        'Unrelated type, not involved in the discriminated union'
    )


class Response(Struct, kw_only=True):
    inner: Annotated[Union[Type1, Type2], Meta(title='Inner')]
