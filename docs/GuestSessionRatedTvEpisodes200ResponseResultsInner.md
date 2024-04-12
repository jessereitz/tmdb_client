# GuestSessionRatedTvEpisodes200ResponseResultsInner


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
**rating** | **float** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.guest_session_rated_tv_episodes200_response_results_inner import GuestSessionRatedTvEpisodes200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GuestSessionRatedTvEpisodes200ResponseResultsInner from a JSON string
guest_session_rated_tv_episodes200_response_results_inner_instance = GuestSessionRatedTvEpisodes200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(GuestSessionRatedTvEpisodes200ResponseResultsInner.to_json())

# convert the object into a dict
guest_session_rated_tv_episodes200_response_results_inner_dict = guest_session_rated_tv_episodes200_response_results_inner_instance.to_dict()
# create an instance of GuestSessionRatedTvEpisodes200ResponseResultsInner from a dict
guest_session_rated_tv_episodes200_response_results_inner_from_dict = GuestSessionRatedTvEpisodes200ResponseResultsInner.from_dict(guest_session_rated_tv_episodes200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


