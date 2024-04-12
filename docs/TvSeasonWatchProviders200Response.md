# TvSeasonWatchProviders200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**results** | [**TvSeasonWatchProviders200ResponseResults**](TvSeasonWatchProviders200ResponseResults.md) |  | [optional] 

## Example

```python
from openapi_client.models.tv_season_watch_providers200_response import TvSeasonWatchProviders200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonWatchProviders200Response from a JSON string
tv_season_watch_providers200_response_instance = TvSeasonWatchProviders200Response.from_json(json)
# print the JSON string representation of the object
print(TvSeasonWatchProviders200Response.to_json())

# convert the object into a dict
tv_season_watch_providers200_response_dict = tv_season_watch_providers200_response_instance.to_dict()
# create an instance of TvSeasonWatchProviders200Response from a dict
tv_season_watch_providers200_response_from_dict = TvSeasonWatchProviders200Response.from_dict(tv_season_watch_providers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


