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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class TvSeriesLatestId200ResponseSeasonsInner(BaseModel):
    """
    TvSeriesLatestId200ResponseSeasonsInner
    """ # noqa: E501
    air_date: Optional[Any] = None
    episode_count: Optional[StrictInt] = 0
    id: Optional[StrictInt] = 0
    name: Optional[StrictStr] = None
    overview: Optional[StrictStr] = None
    poster_path: Optional[Any] = None
    season_number: Optional[StrictInt] = 0
    __properties: ClassVar[List[str]] = ["air_date", "episode_count", "id", "name", "overview", "poster_path", "season_number"]

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
        """Create an instance of TvSeriesLatestId200ResponseSeasonsInner from a JSON string"""
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
        # set to None if air_date (nullable) is None
        # and model_fields_set contains the field
        if self.air_date is None and "air_date" in self.model_fields_set:
            _dict['air_date'] = None

        # set to None if poster_path (nullable) is None
        # and model_fields_set contains the field
        if self.poster_path is None and "poster_path" in self.model_fields_set:
            _dict['poster_path'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TvSeriesLatestId200ResponseSeasonsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "air_date": obj.get("air_date"),
            "episode_count": obj.get("episode_count") if obj.get("episode_count") is not None else 0,
            "id": obj.get("id") if obj.get("id") is not None else 0,
            "name": obj.get("name"),
            "overview": obj.get("overview"),
            "poster_path": obj.get("poster_path"),
            "season_number": obj.get("season_number") if obj.get("season_number") is not None else 0
        })
        return _obj


