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
from openapi_client.models.search_keyword200_response_results_inner import SearchKeyword200ResponseResultsInner
from typing import Optional, Set
from typing_extensions import Self

class SearchKeyword200Response(BaseModel):
    """
    SearchKeyword200Response
    """ # noqa: E501
    page: Optional[StrictInt] = 0
    results: Optional[List[SearchKeyword200ResponseResultsInner]] = None
    total_pages: Optional[StrictInt] = 0
    total_results: Optional[StrictInt] = 0
    __properties: ClassVar[List[str]] = ["page", "results", "total_pages", "total_results"]

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
        """Create an instance of SearchKeyword200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item in self.results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['results'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SearchKeyword200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "page": obj.get("page") if obj.get("page") is not None else 0,
            "results": [SearchKeyword200ResponseResultsInner.from_dict(_item) for _item in obj["results"]] if obj.get("results") is not None else None,
            "total_pages": obj.get("total_pages") if obj.get("total_pages") is not None else 0,
            "total_results": obj.get("total_results") if obj.get("total_results") is not None else 0
        })
        return _obj


