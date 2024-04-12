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

class TvSeriesCredits200ResponseCrewInner(BaseModel):
    """
    TvSeriesCredits200ResponseCrewInner
    """ # noqa: E501
    adult: Optional[StrictBool] = True
    gender: Optional[StrictInt] = 0
    id: Optional[StrictInt] = 0
    known_for_department: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    original_name: Optional[StrictStr] = None
    popularity: Optional[Union[StrictFloat, StrictInt]] = 0
    profile_path: Optional[StrictStr] = None
    credit_id: Optional[StrictStr] = None
    department: Optional[StrictStr] = None
    job: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["adult", "gender", "id", "known_for_department", "name", "original_name", "popularity", "profile_path", "credit_id", "department", "job"]

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
        """Create an instance of TvSeriesCredits200ResponseCrewInner from a JSON string"""
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
        """Create an instance of TvSeriesCredits200ResponseCrewInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "adult": obj.get("adult") if obj.get("adult") is not None else True,
            "gender": obj.get("gender") if obj.get("gender") is not None else 0,
            "id": obj.get("id") if obj.get("id") is not None else 0,
            "known_for_department": obj.get("known_for_department"),
            "name": obj.get("name"),
            "original_name": obj.get("original_name"),
            "popularity": obj.get("popularity") if obj.get("popularity") is not None else 0,
            "profile_path": obj.get("profile_path"),
            "credit_id": obj.get("credit_id"),
            "department": obj.get("department"),
            "job": obj.get("job")
        })
        return _obj


