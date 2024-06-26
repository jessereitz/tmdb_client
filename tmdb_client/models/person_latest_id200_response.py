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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class PersonLatestId200Response(BaseModel):
    """
    PersonLatestId200Response
    """ # noqa: E501
    adult: Optional[StrictBool] = True
    also_known_as: Optional[List[StrictStr]] = None
    biography: Optional[StrictStr] = None
    birthday: Optional[Any] = None
    deathday: Optional[Any] = None
    gender: Optional[StrictInt] = 0
    homepage: Optional[Any] = None
    id: Optional[StrictInt] = 0
    imdb_id: Optional[Any] = None
    known_for_department: Optional[Any] = None
    name: Optional[StrictStr] = None
    place_of_birth: Optional[Any] = None
    popularity: Optional[StrictInt] = 0
    profile_path: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["adult", "also_known_as", "biography", "birthday", "deathday", "gender", "homepage", "id", "imdb_id", "known_for_department", "name", "place_of_birth", "popularity", "profile_path"]

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
        """Create an instance of PersonLatestId200Response from a JSON string"""
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
        # set to None if birthday (nullable) is None
        # and model_fields_set contains the field
        if self.birthday is None and "birthday" in self.model_fields_set:
            _dict['birthday'] = None

        # set to None if deathday (nullable) is None
        # and model_fields_set contains the field
        if self.deathday is None and "deathday" in self.model_fields_set:
            _dict['deathday'] = None

        # set to None if homepage (nullable) is None
        # and model_fields_set contains the field
        if self.homepage is None and "homepage" in self.model_fields_set:
            _dict['homepage'] = None

        # set to None if imdb_id (nullable) is None
        # and model_fields_set contains the field
        if self.imdb_id is None and "imdb_id" in self.model_fields_set:
            _dict['imdb_id'] = None

        # set to None if known_for_department (nullable) is None
        # and model_fields_set contains the field
        if self.known_for_department is None and "known_for_department" in self.model_fields_set:
            _dict['known_for_department'] = None

        # set to None if place_of_birth (nullable) is None
        # and model_fields_set contains the field
        if self.place_of_birth is None and "place_of_birth" in self.model_fields_set:
            _dict['place_of_birth'] = None

        # set to None if profile_path (nullable) is None
        # and model_fields_set contains the field
        if self.profile_path is None and "profile_path" in self.model_fields_set:
            _dict['profile_path'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PersonLatestId200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "adult": obj.get("adult") if obj.get("adult") is not None else True,
            "also_known_as": obj.get("also_known_as"),
            "biography": obj.get("biography"),
            "birthday": obj.get("birthday"),
            "deathday": obj.get("deathday"),
            "gender": obj.get("gender") if obj.get("gender") is not None else 0,
            "homepage": obj.get("homepage"),
            "id": obj.get("id") if obj.get("id") is not None else 0,
            "imdb_id": obj.get("imdb_id"),
            "known_for_department": obj.get("known_for_department"),
            "name": obj.get("name"),
            "place_of_birth": obj.get("place_of_birth"),
            "popularity": obj.get("popularity") if obj.get("popularity") is not None else 0,
            "profile_path": obj.get("profile_path")
        })
        return _obj


