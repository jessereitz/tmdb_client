# TvSeasonDetails200ResponseEpisodesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**air_date** | **str** |  | [optional] 
**episode_number** | **int** |  | [optional] [default to 0]
**id** | **int** |  | [optional] [default to 0]
**name** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**production_code** | **str** |  | [optional] 
**runtime** | **int** |  | [optional] [default to 0]
**season_number** | **int** |  | [optional] [default to 0]
**show_id** | **int** |  | [optional] [default to 0]
**still_path** | **str** |  | [optional] 
**vote_average** | **float** |  | [optional] [default to 0]
**vote_count** | **int** |  | [optional] [default to 0]
**crew** | [**List[TvSeasonDetails200ResponseEpisodesInnerCrewInner]**](TvSeasonDetails200ResponseEpisodesInnerCrewInner.md) |  | [optional] 
**guest_stars** | [**List[TvSeasonDetails200ResponseEpisodesInnerGuestStarsInner]**](TvSeasonDetails200ResponseEpisodesInnerGuestStarsInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_details200_response_episodes_inner import TvSeasonDetails200ResponseEpisodesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonDetails200ResponseEpisodesInner from a JSON string
tv_season_details200_response_episodes_inner_instance = TvSeasonDetails200ResponseEpisodesInner.from_json(json)
# print the JSON string representation of the object
print(TvSeasonDetails200ResponseEpisodesInner.to_json())

# convert the object into a dict
tv_season_details200_response_episodes_inner_dict = tv_season_details200_response_episodes_inner_instance.to_dict()
# create an instance of TvSeasonDetails200ResponseEpisodesInner from a dict
tv_season_details200_response_episodes_inner_from_dict = TvSeasonDetails200ResponseEpisodesInner.from_dict(tv_season_details200_response_episodes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


