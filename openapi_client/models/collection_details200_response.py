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
from openapi_client.models.collection_details200_response_parts_inner import CollectionDetails200ResponsePartsInner
from typing import Optional, Set
from typing_extensions import Self

class CollectionDetails200Response(BaseModel):
    """
    CollectionDetails200Response
    """ # noqa: E501
    id: Optional[StrictInt] = 0
    name: Optional[StrictStr] = None
    overview: Optional[StrictStr] = None
    poster_path: Optional[StrictStr] = None
    backdrop_path: Optional[StrictStr] = None
    parts: Optional[List[CollectionDetails200ResponsePartsInner]] = None
    __properties: ClassVar[List[str]] = ["id", "name", "overview", "poster_path", "backdrop_path", "parts"]

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
        """Create an instance of CollectionDetails200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in parts (list)
        _items = []
        if self.parts:
            for _item in self.parts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['parts'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CollectionDetails200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id") if obj.get("id") is not None else 0,
            "name": obj.get("name"),
            "overview": obj.get("overview"),
            "poster_path": obj.get("poster_path"),
            "backdrop_path": obj.get("backdrop_path"),
            "parts": [CollectionDetails200ResponsePartsInner.from_dict(_item) for _item in obj["parts"]] if obj.get("parts") is not None else None
        })
        return _obj


