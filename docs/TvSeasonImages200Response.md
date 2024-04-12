# TvSeasonImages200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**posters** | [**List[TvSeasonImages200ResponsePostersInner]**](TvSeasonImages200ResponsePostersInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.tv_season_images200_response import TvSeasonImages200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonImages200Response from a JSON string
tv_season_images200_response_instance = TvSeasonImages200Response.from_json(json)
# print the JSON string representation of the object
print(TvSeasonImages200Response.to_json())

# convert the object into a dict
tv_season_images200_response_dict = tv_season_images200_response_instance.to_dict()
# create an instance of TvSeasonImages200Response from a dict
tv_season_images200_response_from_dict = TvSeasonImages200Response.from_dict(tv_season_images200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


