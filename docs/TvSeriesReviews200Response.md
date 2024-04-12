# TvSeriesReviews200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**page** | **int** |  | [optional] [default to 0]
**results** | [**List[TvSeriesReviews200ResponseResultsInner]**](TvSeriesReviews200ResponseResultsInner.md) |  | [optional] 
**total_pages** | **int** |  | [optional] [default to 0]
**total_results** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.tv_series_reviews200_response import TvSeriesReviews200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesReviews200Response from a JSON string
tv_series_reviews200_response_instance = TvSeriesReviews200Response.from_json(json)
# print the JSON string representation of the object
print(TvSeriesReviews200Response.to_json())

# convert the object into a dict
tv_series_reviews200_response_dict = tv_series_reviews200_response_instance.to_dict()
# create an instance of TvSeriesReviews200Response from a dict
tv_series_reviews200_response_from_dict = TvSeriesReviews200Response.from_dict(tv_series_reviews200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


