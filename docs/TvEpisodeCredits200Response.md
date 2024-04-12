# TvEpisodeCredits200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cast** | [**List[TvSeriesCredits200ResponseCastInner]**](TvSeriesCredits200ResponseCastInner.md) |  | [optional] 
**crew** | [**List[TvEpisodeCredits200ResponseCrewInner]**](TvEpisodeCredits200ResponseCrewInner.md) |  | [optional] 
**guest_stars** | [**List[TvEpisodeCredits200ResponseGuestStarsInner]**](TvEpisodeCredits200ResponseGuestStarsInner.md) |  | [optional] 
**id** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.tv_episode_credits200_response import TvEpisodeCredits200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TvEpisodeCredits200Response from a JSON string
tv_episode_credits200_response_instance = TvEpisodeCredits200Response.from_json(json)
# print the JSON string representation of the object
print(TvEpisodeCredits200Response.to_json())

# convert the object into a dict
tv_episode_credits200_response_dict = tv_episode_credits200_response_instance.to_dict()
# create an instance of TvEpisodeCredits200Response from a dict
tv_episode_credits200_response_from_dict = TvEpisodeCredits200Response.from_dict(tv_episode_credits200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


