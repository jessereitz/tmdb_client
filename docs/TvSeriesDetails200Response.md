# TvSeriesDetails200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] [default to True]
**backdrop_path** | **str** |  | [optional] 
**created_by** | [**List[TvSeriesDetails200ResponseCreatedByInner]**](TvSeriesDetails200ResponseCreatedByInner.md) |  | [optional] 
**episode_run_time** | **List[int]** |  | [optional] 
**first_air_date** | **str** |  | [optional] 
**genres** | [**List[TvSeriesDetails200ResponseGenresInner]**](TvSeriesDetails200ResponseGenresInner.md) |  | [optional] 
**homepage** | **str** |  | [optional] 
**id** | **int** |  | [optional] [default to 0]
**in_production** | **bool** |  | [optional] [default to True]
**languages** | **List[str]** |  | [optional] 
**last_air_date** | **str** |  | [optional] 
**last_episode_to_air** | [**TvSeriesDetails200ResponseLastEpisodeToAir**](TvSeriesDetails200ResponseLastEpisodeToAir.md) |  | [optional] 
**name** | **str** |  | [optional] 
**next_episode_to_air** | **object** |  | [optional] 
**networks** | [**List[TvSeriesDetails200ResponseNetworksInner]**](TvSeriesDetails200ResponseNetworksInner.md) |  | [optional] 
**number_of_episodes** | **int** |  | [optional] [default to 0]
**number_of_seasons** | **int** |  | [optional] [default to 0]
**origin_country** | **List[str]** |  | [optional] 
**original_language** | **str** |  | [optional] 
**original_name** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**popularity** | **float** |  | [optional] [default to 0]
**poster_path** | **str** |  | [optional] 
**production_companies** | [**List[TvSeriesDetails200ResponseProductionCompaniesInner]**](TvSeriesDetails200ResponseProductionCompaniesInner.md) |  | [optional] 
**production_countries** | [**List[TvSeriesDetails200ResponseProductionCountriesInner]**](TvSeriesDetails200ResponseProductionCountriesInner.md) |  | [optional] 
**seasons** | [**List[TvSeriesDetails200ResponseSeasonsInner]**](TvSeriesDetails200ResponseSeasonsInner.md) |  | [optional] 
**spoken_languages** | [**List[MovieDetails200ResponseSpokenLanguagesInner]**](MovieDetails200ResponseSpokenLanguagesInner.md) |  | [optional] 
**status** | **str** |  | [optional] 
**tagline** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**vote_average** | **float** |  | [optional] [default to 0]
**vote_count** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.tv_series_details200_response import TvSeriesDetails200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesDetails200Response from a JSON string
tv_series_details200_response_instance = TvSeriesDetails200Response.from_json(json)
# print the JSON string representation of the object
print(TvSeriesDetails200Response.to_json())

# convert the object into a dict
tv_series_details200_response_dict = tv_series_details200_response_instance.to_dict()
# create an instance of TvSeriesDetails200Response from a dict
tv_series_details200_response_from_dict = TvSeriesDetails200Response.from_dict(tv_series_details200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


