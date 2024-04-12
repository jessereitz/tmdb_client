# TvSeriesDetails200ResponseSeasonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**air_date** | **str** |  | [optional] 
**episode_count** | **int** |  | [optional] [default to 0]
**id** | **int** |  | [optional] [default to 0]
**name** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**poster_path** | **str** |  | [optional] 
**season_number** | **int** |  | [optional] [default to 0]
**vote_average** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.tv_series_details200_response_seasons_inner import TvSeriesDetails200ResponseSeasonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesDetails200ResponseSeasonsInner from a JSON string
tv_series_details200_response_seasons_inner_instance = TvSeriesDetails200ResponseSeasonsInner.from_json(json)
# print the JSON string representation of the object
print(TvSeriesDetails200ResponseSeasonsInner.to_json())

# convert the object into a dict
tv_series_details200_response_seasons_inner_dict = tv_series_details200_response_seasons_inner_instance.to_dict()
# create an instance of TvSeriesDetails200ResponseSeasonsInner from a dict
tv_series_details200_response_seasons_inner_from_dict = TvSeriesDetails200ResponseSeasonsInner.from_dict(tv_series_details200_response_seasons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


