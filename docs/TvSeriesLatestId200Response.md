# TvSeriesLatestId200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] [default to True]
**backdrop_path** | **object** |  | [optional] 
**created_by** | **List[str]** |  | [optional] 
**episode_run_time** | **List[str]** |  | [optional] 
**first_air_date** | **str** |  | [optional] 
**genres** | **List[str]** |  | [optional] 
**homepage** | **str** |  | [optional] 
**id** | **int** |  | [optional] [default to 0]
**in_production** | **bool** |  | [optional] [default to True]
**languages** | **List[str]** |  | [optional] 
**last_air_date** | **str** |  | [optional] 
**last_episode_to_air** | [**TvSeriesLatestId200ResponseLastEpisodeToAir**](TvSeriesLatestId200ResponseLastEpisodeToAir.md) |  | [optional] 
**name** | **str** |  | [optional] 
**next_episode_to_air** | **object** |  | [optional] 
**networks** | **List[str]** |  | [optional] 
**number_of_episodes** | **int** |  | [optional] [default to 0]
**number_of_seasons** | **int** |  | [optional] [default to 0]
**origin_country** | **List[str]** |  | [optional] 
**original_language** | **str** |  | [optional] 
**original_name** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**popularity** | **int** |  | [optional] [default to 0]
**poster_path** | **object** |  | [optional] 
**production_companies** | **List[str]** |  | [optional] 
**production_countries** | **List[str]** |  | [optional] 
**seasons** | [**List[TvSeriesLatestId200ResponseSeasonsInner]**](TvSeriesLatestId200ResponseSeasonsInner.md) |  | [optional] 
**spoken_languages** | **List[str]** |  | [optional] 
**status** | **str** |  | [optional] 
**tagline** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**vote_average** | **int** |  | [optional] [default to 0]
**vote_count** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.tv_series_latest_id200_response import TvSeriesLatestId200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesLatestId200Response from a JSON string
tv_series_latest_id200_response_instance = TvSeriesLatestId200Response.from_json(json)
# print the JSON string representation of the object
print(TvSeriesLatestId200Response.to_json())

# convert the object into a dict
tv_series_latest_id200_response_dict = tv_series_latest_id200_response_instance.to_dict()
# create an instance of TvSeriesLatestId200Response from a dict
tv_series_latest_id200_response_from_dict = TvSeriesLatestId200Response.from_dict(tv_series_latest_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


