# TvEpisodeDetails200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**air_date** | **str** |  | [optional] 
**crew** | [**List[TvEpisodeDetails200ResponseCrewInner]**](TvEpisodeDetails200ResponseCrewInner.md) |  | [optional] 
**episode_number** | **int** |  | [optional] [default to 0]
**guest_stars** | [**List[TvEpisodeDetails200ResponseGuestStarsInner]**](TvEpisodeDetails200ResponseGuestStarsInner.md) |  | [optional] 
**name** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**id** | **int** |  | [optional] [default to 0]
**production_code** | **str** |  | [optional] 
**runtime** | **int** |  | [optional] [default to 0]
**season_number** | **int** |  | [optional] [default to 0]
**still_path** | **str** |  | [optional] 
**vote_average** | **float** |  | [optional] [default to 0]
**vote_count** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.tv_episode_details200_response import TvEpisodeDetails200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TvEpisodeDetails200Response from a JSON string
tv_episode_details200_response_instance = TvEpisodeDetails200Response.from_json(json)
# print the JSON string representation of the object
print(TvEpisodeDetails200Response.to_json())

# convert the object into a dict
tv_episode_details200_response_dict = tv_episode_details200_response_instance.to_dict()
# create an instance of TvEpisodeDetails200Response from a dict
tv_episode_details200_response_from_dict = TvEpisodeDetails200Response.from_dict(tv_episode_details200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


