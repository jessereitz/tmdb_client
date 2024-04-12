# TvSeriesTopRatedList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] [default to 0]
**results** | [**List[TvSeriesTopRatedList200ResponseResultsInner]**](TvSeriesTopRatedList200ResponseResultsInner.md) |  | [optional] 
**total_pages** | **int** |  | [optional] [default to 0]
**total_results** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.tv_series_top_rated_list200_response import TvSeriesTopRatedList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesTopRatedList200Response from a JSON string
tv_series_top_rated_list200_response_instance = TvSeriesTopRatedList200Response.from_json(json)
# print the JSON string representation of the object
print(TvSeriesTopRatedList200Response.to_json())

# convert the object into a dict
tv_series_top_rated_list200_response_dict = tv_series_top_rated_list200_response_instance.to_dict()
# create an instance of TvSeriesTopRatedList200Response from a dict
tv_series_top_rated_list200_response_from_dict = TvSeriesTopRatedList200Response.from_dict(tv_series_top_rated_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


