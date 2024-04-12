# TvSeriesDetails200ResponseGenresInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**name** | **str** |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_details200_response_genres_inner import TvSeriesDetails200ResponseGenresInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesDetails200ResponseGenresInner from a JSON string
tv_series_details200_response_genres_inner_instance = TvSeriesDetails200ResponseGenresInner.from_json(json)
# print the JSON string representation of the object
print(TvSeriesDetails200ResponseGenresInner.to_json())

# convert the object into a dict
tv_series_details200_response_genres_inner_dict = tv_series_details200_response_genres_inner_instance.to_dict()
# create an instance of TvSeriesDetails200ResponseGenresInner from a dict
tv_series_details200_response_genres_inner_from_dict = TvSeriesDetails200ResponseGenresInner.from_dict(tv_series_details200_response_genres_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


