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
from tmdb_client.models.movie_details200_response_spoken_languages_inner import MovieDetails200ResponseSpokenLanguagesInner
from tmdb_client.models.tv_series_details200_response_created_by_inner import TvSeriesDetails200ResponseCreatedByInner
from tmdb_client.models.tv_series_details200_response_genres_inner import TvSeriesDetails200ResponseGenresInner
from tmdb_client.models.tv_series_details200_response_last_episode_to_air import TvSeriesDetails200ResponseLastEpisodeToAir
from tmdb_client.models.tv_series_details200_response_networks_inner import TvSeriesDetails200ResponseNetworksInner
from tmdb_client.models.tv_series_details200_response_production_companies_inner import TvSeriesDetails200ResponseProductionCompaniesInner
from tmdb_client.models.tv_series_details200_response_production_countries_inner import TvSeriesDetails200ResponseProductionCountriesInner
from tmdb_client.models.tv_series_details200_response_seasons_inner import TvSeriesDetails200ResponseSeasonsInner
from typing import Optional, Set
from typing_extensions import Self

class TvSeriesDetails200Response(BaseModel):
    """
    TvSeriesDetails200Response
    """ # noqa: E501
    adult: Optional[StrictBool] = True
    backdrop_path: Optional[StrictStr] = None
    created_by: Optional[List[TvSeriesDetails200ResponseCreatedByInner]] = None
    episode_run_time: Optional[List[StrictInt]] = None
    first_air_date: Optional[StrictStr] = None
    genres: Optional[List[TvSeriesDetails200ResponseGenresInner]] = None
    homepage: Optional[StrictStr] = None
    id: Optional[StrictInt] = 0
    in_production: Optional[StrictBool] = True
    languages: Optional[List[StrictStr]] = None
    last_air_date: Optional[StrictStr] = None
    last_episode_to_air: Optional[TvSeriesDetails200ResponseLastEpisodeToAir] = None
    name: Optional[StrictStr] = None
    next_episode_to_air: Optional[Any] = None
    networks: Optional[List[TvSeriesDetails200ResponseNetworksInner]] = None
    number_of_episodes: Optional[StrictInt] = 0
    number_of_seasons: Optional[StrictInt] = 0
    origin_country: Optional[List[StrictStr]] = None
    original_language: Optional[StrictStr] = None
    original_name: Optional[StrictStr] = None
    overview: Optional[StrictStr] = None
    popularity: Optional[Union[StrictFloat, StrictInt]] = 0
    poster_path: Optional[StrictStr] = None
    production_companies: Optional[List[TvSeriesDetails200ResponseProductionCompaniesInner]] = None
    production_countries: Optional[List[TvSeriesDetails200ResponseProductionCountriesInner]] = None
    seasons: Optional[List[TvSeriesDetails200ResponseSeasonsInner]] = None
    spoken_languages: Optional[List[MovieDetails200ResponseSpokenLanguagesInner]] = None
    status: Optional[StrictStr] = None
    tagline: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    vote_average: Optional[Union[StrictFloat, StrictInt]] = 0
    vote_count: Optional[StrictInt] = 0
    __properties: ClassVar[List[str]] = ["adult", "backdrop_path", "created_by", "episode_run_time", "first_air_date", "genres", "homepage", "id", "in_production", "languages", "last_air_date", "last_episode_to_air", "name", "next_episode_to_air", "networks", "number_of_episodes", "number_of_seasons", "origin_country", "original_language", "original_name", "overview", "popularity", "poster_path", "production_companies", "production_countries", "seasons", "spoken_languages", "status", "tagline", "type", "vote_average", "vote_count"]

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
        """Create an instance of TvSeriesDetails200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in created_by (list)
        _items = []
        if self.created_by:
            for _item in self.created_by:
                if _item:
                    _items.append(_item.to_dict())
            _dict['created_by'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in genres (list)
        _items = []
        if self.genres:
            for _item in self.genres:
                if _item:
                    _items.append(_item.to_dict())
            _dict['genres'] = _items
        # override the default output from pydantic by calling `to_dict()` of last_episode_to_air
        if self.last_episode_to_air:
            _dict['last_episode_to_air'] = self.last_episode_to_air.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in networks (list)
        _items = []
        if self.networks:
            for _item in self.networks:
                if _item:
                    _items.append(_item.to_dict())
            _dict['networks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in production_companies (list)
        _items = []
        if self.production_companies:
            for _item in self.production_companies:
                if _item:
                    _items.append(_item.to_dict())
            _dict['production_companies'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in production_countries (list)
        _items = []
        if self.production_countries:
            for _item in self.production_countries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['production_countries'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in seasons (list)
        _items = []
        if self.seasons:
            for _item in self.seasons:
                if _item:
                    _items.append(_item.to_dict())
            _dict['seasons'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in spoken_languages (list)
        _items = []
        if self.spoken_languages:
            for _item in self.spoken_languages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['spoken_languages'] = _items
        # set to None if next_episode_to_air (nullable) is None
        # and model_fields_set contains the field
        if self.next_episode_to_air is None and "next_episode_to_air" in self.model_fields_set:
            _dict['next_episode_to_air'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TvSeriesDetails200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "adult": obj.get("adult") if obj.get("adult") is not None else True,
            "backdrop_path": obj.get("backdrop_path"),
            "created_by": [TvSeriesDetails200ResponseCreatedByInner.from_dict(_item) for _item in obj["created_by"]] if obj.get("created_by") is not None else None,
            "episode_run_time": obj.get("episode_run_time"),
            "first_air_date": obj.get("first_air_date"),
            "genres": [TvSeriesDetails200ResponseGenresInner.from_dict(_item) for _item in obj["genres"]] if obj.get("genres") is not None else None,
            "homepage": obj.get("homepage"),
            "id": obj.get("id") if obj.get("id") is not None else 0,
            "in_production": obj.get("in_production") if obj.get("in_production") is not None else True,
            "languages": obj.get("languages"),
            "last_air_date": obj.get("last_air_date"),
            "last_episode_to_air": TvSeriesDetails200ResponseLastEpisodeToAir.from_dict(obj["last_episode_to_air"]) if obj.get("last_episode_to_air") is not None else None,
            "name": obj.get("name"),
            "next_episode_to_air": obj.get("next_episode_to_air"),
            "networks": [TvSeriesDetails200ResponseNetworksInner.from_dict(_item) for _item in obj["networks"]] if obj.get("networks") is not None else None,
            "number_of_episodes": obj.get("number_of_episodes") if obj.get("number_of_episodes") is not None else 0,
            "number_of_seasons": obj.get("number_of_seasons") if obj.get("number_of_seasons") is not None else 0,
            "origin_country": obj.get("origin_country"),
            "original_language": obj.get("original_language"),
            "original_name": obj.get("original_name"),
            "overview": obj.get("overview"),
            "popularity": obj.get("popularity") if obj.get("popularity") is not None else 0,
            "poster_path": obj.get("poster_path"),
            "production_companies": [TvSeriesDetails200ResponseProductionCompaniesInner.from_dict(_item) for _item in obj["production_companies"]] if obj.get("production_companies") is not None else None,
            "production_countries": [TvSeriesDetails200ResponseProductionCountriesInner.from_dict(_item) for _item in obj["production_countries"]] if obj.get("production_countries") is not None else None,
            "seasons": [TvSeriesDetails200ResponseSeasonsInner.from_dict(_item) for _item in obj["seasons"]] if obj.get("seasons") is not None else None,
            "spoken_languages": [MovieDetails200ResponseSpokenLanguagesInner.from_dict(_item) for _item in obj["spoken_languages"]] if obj.get("spoken_languages") is not None else None,
            "status": obj.get("status"),
            "tagline": obj.get("tagline"),
            "type": obj.get("type"),
            "vote_average": obj.get("vote_average") if obj.get("vote_average") is not None else 0,
            "vote_count": obj.get("vote_count") if obj.get("vote_count") is not None else 0
        })
        return _obj


