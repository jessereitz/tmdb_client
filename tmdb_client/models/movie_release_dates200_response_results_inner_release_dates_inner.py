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

class MovieReleaseDates200ResponseResultsInnerReleaseDatesInner(BaseModel):
    """
    MovieReleaseDates200ResponseResultsInnerReleaseDatesInner
    """ # noqa: E501
    certification: Optional[StrictStr] = None
    descriptors: Optional[List[StrictStr]] = None
    iso_639_1: Optional[StrictStr] = None
    note: Optional[StrictStr] = None
    release_date: Optional[StrictStr] = None
    type: Optional[StrictInt] = 0
    __properties: ClassVar[List[str]] = ["certification", "descriptors", "iso_639_1", "note", "release_date", "type"]

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
        """Create an instance of MovieReleaseDates200ResponseResultsInnerReleaseDatesInner from a JSON string"""
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
        """Create an instance of MovieReleaseDates200ResponseResultsInnerReleaseDatesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "certification": obj.get("certification"),
            "descriptors": obj.get("descriptors"),
            "iso_639_1": obj.get("iso_639_1"),
            "note": obj.get("note"),
            "release_date": obj.get("release_date"),
            "type": obj.get("type") if obj.get("type") is not None else 0
        })
        return _obj

