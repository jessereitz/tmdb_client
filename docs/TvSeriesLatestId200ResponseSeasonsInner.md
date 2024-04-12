# TvSeriesLatestId200ResponseSeasonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**air_date** | **object** |  | [optional] 
**episode_count** | **int** |  | [optional] [default to 0]
**id** | **int** |  | [optional] [default to 0]
**name** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**poster_path** | **object** |  | [optional] 
**season_number** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.tv_series_latest_id200_response_seasons_inner import TvSeriesLatestId200ResponseSeasonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesLatestId200ResponseSeasonsInner from a JSON string
tv_series_latest_id200_response_seasons_inner_instance = TvSeriesLatestId200ResponseSeasonsInner.from_json(json)
# print the JSON string representation of the object
print(TvSeriesLatestId200ResponseSeasonsInner.to_json())

# convert the object into a dict
tv_series_latest_id200_response_seasons_inner_dict = tv_series_latest_id200_response_seasons_inner_instance.to_dict()
# create an instance of TvSeriesLatestId200ResponseSeasonsInner from a dict
tv_series_latest_id200_response_seasons_inner_from_dict = TvSeriesLatestId200ResponseSeasonsInner.from_dict(tv_series_latest_id200_response_seasons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


