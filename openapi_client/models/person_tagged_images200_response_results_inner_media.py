# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class PersonTaggedImages200ResponseResultsInnerMedia(BaseModel):
    """
    PersonTaggedImages200ResponseResultsInnerMedia
    """ # noqa: E501
    adult: Optional[StrictBool] = True
    backdrop_path: Optional[StrictStr] = None
    id: Optional[StrictInt] = 0
    title: Optional[StrictStr] = None
    original_language: Optional[StrictStr] = None
    original_title: Optional[StrictStr] = None
    overview: Optional[StrictStr] = None
    poster_path: Optional[StrictStr] = None
    media_type: Optional[StrictStr] = None
    genre_ids: Optional[List[StrictInt]] = None
    popularity: Optional[Union[StrictFloat, StrictInt]] = 0
    release_date: Optional[StrictStr] = None
    video: Optional[StrictBool] = True
    vote_average: Optional[Union[StrictFloat, StrictInt]] = 0
    vote_count: Optional[StrictInt] = 0
    __properties: ClassVar[List[str]] = ["adult", "backdrop_path", "id", "title", "original_language", "original_title", "overview", "poster_path", "media_type", "genre_ids", "popularity", "release_date", "video", "vote_average", "vote_count"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PersonTaggedImages200ResponseResultsInnerMedia from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PersonTaggedImages200ResponseResultsInnerMedia from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "adult": obj.get("adult") if obj.get("adult") is not None else True,
            "backdrop_path": obj.get("backdrop_path"),
            "id": obj.get("id") if obj.get("id") is not None else 0,
            "title": obj.get("title"),
            "original_language": obj.get("original_language"),
            "original_title": obj.get("original_title"),
            "overview": obj.get("overview"),
            "poster_path": obj.get("poster_path"),
            "media_type": obj.get("media_type"),
            "genre_ids": obj.get("genre_ids"),
            "popularity": obj.get("popularity") if obj.get("popularity") is not None else 0,
            "release_date": obj.get("release_date"),
            "video": obj.get("video") if obj.get("video") is not None else True,
            "vote_average": obj.get("vote_average") if obj.get("vote_average") is not None else 0,
            "vote_count": obj.get("vote_count") if obj.get("vote_count") is not None else 0
        })
        return _obj


