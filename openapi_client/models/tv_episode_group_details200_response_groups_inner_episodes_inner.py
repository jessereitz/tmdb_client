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

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class TvEpisodeGroupDetails200ResponseGroupsInnerEpisodesInner(BaseModel):
    """
    TvEpisodeGroupDetails200ResponseGroupsInnerEpisodesInner
    """ # noqa: E501
    air_date: Optional[StrictStr] = None
    episode_number: Optional[StrictInt] = 0
    id: Optional[StrictInt] = 0
    name: Optional[StrictStr] = None
    overview: Optional[StrictStr] = None
    production_code: Optional[StrictStr] = None
    runtime: Optional[Any] = None
    season_number: Optional[StrictInt] = 0
    show_id: Optional[StrictInt] = 0
    still_path: Optional[StrictStr] = None
    vote_average: Optional[Union[StrictFloat, StrictInt]] = 0
    vote_count: Optional[StrictInt] = 0
    order: Optional[StrictInt] = 0
    __properties: ClassVar[List[str]] = ["air_date", "episode_number", "id", "name", "overview", "production_code", "runtime", "season_number", "show_id", "still_path", "vote_average", "vote_count", "order"]

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
        """Create an instance of TvEpisodeGroupDetails200ResponseGroupsInnerEpisodesInner from a JSON string"""
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
        # set to None if runtime (nullable) is None
        # and model_fields_set contains the field
        if self.runtime is None and "runtime" in self.model_fields_set:
            _dict['runtime'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TvEpisodeGroupDetails200ResponseGroupsInnerEpisodesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "air_date": obj.get("air_date"),
            "episode_number": obj.get("episode_number") if obj.get("episode_number") is not None else 0,
            "id": obj.get("id") if obj.get("id") is not None else 0,
            "name": obj.get("name"),
            "overview": obj.get("overview"),
            "production_code": obj.get("production_code"),
            "runtime": obj.get("runtime"),
            "season_number": obj.get("season_number") if obj.get("season_number") is not None else 0,
            "show_id": obj.get("show_id") if obj.get("show_id") is not None else 0,
            "still_path": obj.get("still_path"),
            "vote_average": obj.get("vote_average") if obj.get("vote_average") is not None else 0,
            "vote_count": obj.get("vote_count") if obj.get("vote_count") is not None else 0,
            "order": obj.get("order") if obj.get("order") is not None else 0
        })
        return _obj


