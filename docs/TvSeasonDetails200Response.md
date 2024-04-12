# TvSeasonDetails200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**air_date** | **str** |  | [optional] 
**episodes** | [**List[TvSeasonDetails200ResponseEpisodesInner]**](TvSeasonDetails200ResponseEpisodesInner.md) |  | [optional] 
**name** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**id** | **int** |  | [optional] [default to 0]
**poster_path** | **str** |  | [optional] 
**season_number** | **int** |  | [optional] [default to 0]
**vote_average** | **float** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.tv_season_details200_response import TvSeasonDetails200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonDetails200Response from a JSON string
tv_season_details200_response_instance = TvSeasonDetails200Response.from_json(json)
# print the JSON string representation of the object
print(TvSeasonDetails200Response.to_json())

# convert the object into a dict
tv_season_details200_response_dict = tv_season_details200_response_instance.to_dict()
# create an instance of TvSeasonDetails200Response from a dict
tv_season_details200_response_from_dict = TvSeasonDetails200Response.from_dict(tv_season_details200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


