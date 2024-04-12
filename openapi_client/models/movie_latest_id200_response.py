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

class MovieLatestId200Response(BaseModel):
    """
    MovieLatestId200Response
    """ # noqa: E501
    adult: Optional[StrictBool] = True
    backdrop_path: Optional[Any] = None
    belongs_to_collection: Optional[Any] = None
    budget: Optional[StrictInt] = 0
    genres: Optional[List[StrictStr]] = None
    homepage: Optional[StrictStr] = None
    id: Optional[StrictInt] = 0
    imdb_id: Optional[Any] = None
    original_language: Optional[StrictStr] = None
    original_title: Optional[StrictStr] = None
    overview: Optional[StrictStr] = None
    popularity: Optional[StrictInt] = 0
    poster_path: Optional[Any] = None
    production_companies: Optional[List[StrictStr]] = None
    production_countries: Optional[List[StrictStr]] = None
    release_date: Optional[StrictStr] = None
    revenue: Optional[StrictInt] = 0
    runtime: Optional[StrictInt] = 0
    spoken_languages: Optional[List[StrictStr]] = None
    status: Optional[StrictStr] = None
    tagline: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    video: Optional[StrictBool] = True
    vote_average: Optional[StrictInt] = 0
    vote_count: Optional[StrictInt] = 0
    __properties: ClassVar[List[str]] = ["adult", "backdrop_path", "belongs_to_collection", "budget", "genres", "homepage", "id", "imdb_id", "original_language", "original_title", "overview", "popularity", "poster_path", "production_companies", "production_countries", "release_date", "revenue", "runtime", "spoken_languages", "status", "tagline", "title", "video", "vote_average", "vote_count"]

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
        """Create an instance of MovieLatestId200Response from a JSON string"""
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
        # set to None if backdrop_path (nullable) is None
        # and model_fields_set contains the field
        if self.backdrop_path is None and "backdrop_path" in self.model_fields_set:
            _dict['backdrop_path'] = None

        # set to None if belongs_to_collection (nullable) is None
        # and model_fields_set contains the field
        if self.belongs_to_collection is None and "belongs_to_collection" in self.model_fields_set:
            _dict['belongs_to_collection'] = None

        # set to None if imdb_id (nullable) is None
        # and model_fields_set contains the field
        if self.imdb_id is None and "imdb_id" in self.model_fields_set:
            _dict['imdb_id'] = None

        # set to None if poster_path (nullable) is None
        # and model_fields_set contains the field
        if self.poster_path is None and "poster_path" in self.model_fields_set:
            _dict['poster_path'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MovieLatestId200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "adult": obj.get("adult") if obj.get("adult") is not None else True,
            "backdrop_path": obj.get("backdrop_path"),
            "belongs_to_collection": obj.get("belongs_to_collection"),
            "budget": obj.get("budget") if obj.get("budget") is not None else 0,
            "genres": obj.get("genres"),
            "homepage": obj.get("homepage"),
            "id": obj.get("id") if obj.get("id") is not None else 0,
            "imdb_id": obj.get("imdb_id"),
            "original_language": obj.get("original_language"),
            "original_title": obj.get("original_title"),
            "overview": obj.get("overview"),
            "popularity": obj.get("popularity") if obj.get("popularity") is not None else 0,
            "poster_path": obj.get("poster_path"),
            "production_companies": obj.get("production_companies"),
            "production_countries": obj.get("production_countries"),
            "release_date": obj.get("release_date"),
            "revenue": obj.get("revenue") if obj.get("revenue") is not None else 0,
            "runtime": obj.get("runtime") if obj.get("runtime") is not None else 0,
            "spoken_languages": obj.get("spoken_languages"),
            "status": obj.get("status"),
            "tagline": obj.get("tagline"),
            "title": obj.get("title"),
            "video": obj.get("video") if obj.get("video") is not None else True,
            "vote_average": obj.get("vote_average") if obj.get("vote_average") is not None else 0,
            "vote_count": obj.get("vote_count") if obj.get("vote_count") is not None else 0
        })
        return _obj

