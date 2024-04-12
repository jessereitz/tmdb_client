# TvSeasonImages200ResponsePostersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspect_ratio** | **float** |  | [optional] [default to 0]
**height** | **int** |  | [optional] [default to 0]
**iso_639_1** | **str** |  | [optional] 
**file_path** | **str** |  | [optional] 
**vote_average** | **float** |  | [optional] [default to 0]
**vote_count** | **int** |  | [optional] [default to 0]
**width** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.tv_season_images200_response_posters_inner import TvSeasonImages200ResponsePostersInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonImages200ResponsePostersInner from a JSON string
tv_season_images200_response_posters_inner_instance = TvSeasonImages200ResponsePostersInner.from_json(json)
# print the JSON string representation of the object
print(TvSeasonImages200ResponsePostersInner.to_json())

# convert the object into a dict
tv_season_images200_response_posters_inner_dict = tv_season_images200_response_posters_inner_instance.to_dict()
# create an instance of TvSeasonImages200ResponsePostersInner from a dict
tv_season_images200_response_posters_inner_from_dict = TvSeasonImages200ResponsePostersInner.from_dict(tv_season_images200_response_posters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


