from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SongCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    POP: _ClassVar[SongCategory]
    HIP_HOP: _ClassVar[SongCategory]
    ELECTRONIC: _ClassVar[SongCategory]
    FOLK: _ClassVar[SongCategory]
    ROCK: _ClassVar[SongCategory]
POP: SongCategory
HIP_HOP: SongCategory
ELECTRONIC: SongCategory
FOLK: SongCategory
ROCK: SongCategory

class RecommendationRequest(_message.Message):
    __slots__ = ("category", "max_results")
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    category: SongCategory
    max_results: int
    def __init__(self, category: _Optional[_Union[SongCategory, str]] = ..., max_results: _Optional[int] = ...) -> None: ...

class RecommendationResponse(_message.Message):
    __slots__ = ("recommendations",)
    RECOMMENDATIONS_FIELD_NUMBER: _ClassVar[int]
    recommendations: _containers.RepeatedCompositeFieldContainer[SongRecommendation]
    def __init__(self, recommendations: _Optional[_Iterable[_Union[SongRecommendation, _Mapping]]] = ...) -> None: ...

class SongRecommendation(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
