# TvEpisodeCredits200ResponseGuestStarsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**character** | **str** |  | [optional] 
**credit_id** | **str** |  | [optional] 
**order** | **int** |  | [optional] [default to 0]
**adult** | **bool** |  | [optional] [default to True]
**gender** | **int** |  | [optional] [default to 0]
**id** | **int** |  | [optional] [default to 0]
**known_for_department** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**original_name** | **str** |  | [optional] 
**popularity** | **float** |  | [optional] [default to 0]
**profile_path** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tv_episode_credits200_response_guest_stars_inner import TvEpisodeCredits200ResponseGuestStarsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvEpisodeCredits200ResponseGuestStarsInner from a JSON string
tv_episode_credits200_response_guest_stars_inner_instance = TvEpisodeCredits200ResponseGuestStarsInner.from_json(json)
# print the JSON string representation of the object
print(TvEpisodeCredits200ResponseGuestStarsInner.to_json())

# convert the object into a dict
tv_episode_credits200_response_guest_stars_inner_dict = tv_episode_credits200_response_guest_stars_inner_instance.to_dict()
# create an instance of TvEpisodeCredits200ResponseGuestStarsInner from a dict
tv_episode_credits200_response_guest_stars_inner_from_dict = TvEpisodeCredits200ResponseGuestStarsInner.from_dict(tv_episode_credits200_response_guest_stars_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


