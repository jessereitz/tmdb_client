# TvSeriesDetails200ResponseLastEpisodeToAir


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**name** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**vote_average** | **float** |  | [optional] [default to 0]
**vote_count** | **int** |  | [optional] [default to 0]
**air_date** | **str** |  | [optional] 
**episode_number** | **int** |  | [optional] [default to 0]
**production_code** | **str** |  | [optional] 
**runtime** | **int** |  | [optional] [default to 0]
**season_number** | **int** |  | [optional] [default to 0]
**show_id** | **int** |  | [optional] [default to 0]
**still_path** | **str** |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_details200_response_last_episode_to_air import TvSeriesDetails200ResponseLastEpisodeToAir

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesDetails200ResponseLastEpisodeToAir from a JSON string
tv_series_details200_response_last_episode_to_air_instance = TvSeriesDetails200ResponseLastEpisodeToAir.from_json(json)
# print the JSON string representation of the object
print(TvSeriesDetails200ResponseLastEpisodeToAir.to_json())

# convert the object into a dict
tv_series_details200_response_last_episode_to_air_dict = tv_series_details200_response_last_episode_to_air_instance.to_dict()
# create an instance of TvSeriesDetails200ResponseLastEpisodeToAir from a dict
tv_series_details200_response_last_episode_to_air_from_dict = TvSeriesDetails200ResponseLastEpisodeToAir.from_dict(tv_series_details200_response_last_episode_to_air_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


