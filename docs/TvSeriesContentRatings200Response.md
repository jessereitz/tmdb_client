# TvSeriesContentRatings200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[TvSeriesContentRatings200ResponseResultsInner]**](TvSeriesContentRatings200ResponseResultsInner.md) |  | [optional] 
**id** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.tv_series_content_ratings200_response import TvSeriesContentRatings200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesContentRatings200Response from a JSON string
tv_series_content_ratings200_response_instance = TvSeriesContentRatings200Response.from_json(json)
# print the JSON string representation of the object
print(TvSeriesContentRatings200Response.to_json())

# convert the object into a dict
tv_series_content_ratings200_response_dict = tv_series_content_ratings200_response_instance.to_dict()
# create an instance of TvSeriesContentRatings200Response from a dict
tv_series_content_ratings200_response_from_dict = TvSeriesContentRatings200Response.from_dict(tv_series_content_ratings200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


