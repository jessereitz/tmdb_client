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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.movie_watch_providers200_response_results_au_buy_inner import MovieWatchProviders200ResponseResultsAUBuyInner
from openapi_client.models.tv_series_watch_providers200_response_results_au_flatrate_inner import TvSeriesWatchProviders200ResponseResultsAUFlatrateInner
from typing import Optional, Set
from typing_extensions import Self

class TvSeriesWatchProviders200ResponseResultsAU(BaseModel):
    """
    TvSeriesWatchProviders200ResponseResultsAU
    """ # noqa: E501
    link: Optional[StrictStr] = None
    flatrate: Optional[List[TvSeriesWatchProviders200ResponseResultsAUFlatrateInner]] = None
    buy: Optional[List[MovieWatchProviders200ResponseResultsAUBuyInner]] = None
    __properties: ClassVar[List[str]] = ["link", "flatrate", "buy"]

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
        """Create an instance of TvSeriesWatchProviders200ResponseResultsAU from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in flatrate (list)
        _items = []
        if self.flatrate:
            for _item in self.flatrate:
                if _item:
                    _items.append(_item.to_dict())
            _dict['flatrate'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in buy (list)
        _items = []
        if self.buy:
            for _item in self.buy:
                if _item:
                    _items.append(_item.to_dict())
            _dict['buy'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TvSeriesWatchProviders200ResponseResultsAU from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "link": obj.get("link"),
            "flatrate": [TvSeriesWatchProviders200ResponseResultsAUFlatrateInner.from_dict(_item) for _item in obj["flatrate"]] if obj.get("flatrate") is not None else None,
            "buy": [MovieWatchProviders200ResponseResultsAUBuyInner.from_dict(_item) for _item in obj["buy"]] if obj.get("buy") is not None else None
        })
        return _obj


