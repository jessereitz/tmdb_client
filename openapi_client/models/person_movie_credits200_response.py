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

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.person_movie_credits200_response_cast_inner import PersonMovieCredits200ResponseCastInner
from openapi_client.models.person_movie_credits200_response_crew_inner import PersonMovieCredits200ResponseCrewInner
from typing import Optional, Set
from typing_extensions import Self

class PersonMovieCredits200Response(BaseModel):
    """
    PersonMovieCredits200Response
    """ # noqa: E501
    cast: Optional[List[PersonMovieCredits200ResponseCastInner]] = None
    crew: Optional[List[PersonMovieCredits200ResponseCrewInner]] = None
    id: Optional[StrictInt] = 0
    __properties: ClassVar[List[str]] = ["cast", "crew", "id"]

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
        """Create an instance of PersonMovieCredits200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in cast (list)
        _items = []
        if self.cast:
            for _item in self.cast:
                if _item:
                    _items.append(_item.to_dict())
            _dict['cast'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in crew (list)
        _items = []
        if self.crew:
            for _item in self.crew:
                if _item:
                    _items.append(_item.to_dict())
            _dict['crew'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PersonMovieCredits200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cast": [PersonMovieCredits200ResponseCastInner.from_dict(_item) for _item in obj["cast"]] if obj.get("cast") is not None else None,
            "crew": [PersonMovieCredits200ResponseCrewInner.from_dict(_item) for _item in obj["crew"]] if obj.get("crew") is not None else None,
            "id": obj.get("id") if obj.get("id") is not None else 0
        })
        return _obj


