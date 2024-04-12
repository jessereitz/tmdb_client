# TvSeriesKeywords200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**results** | [**List[MovieKeywords200ResponseKeywordsInner]**](MovieKeywords200ResponseKeywordsInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_keywords200_response import TvSeriesKeywords200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesKeywords200Response from a JSON string
tv_series_keywords200_response_instance = TvSeriesKeywords200Response.from_json(json)
# print the JSON string representation of the object
print(TvSeriesKeywords200Response.to_json())

# convert the object into a dict
tv_series_keywords200_response_dict = tv_series_keywords200_response_instance.to_dict()
# create an instance of TvSeriesKeywords200Response from a dict
tv_series_keywords200_response_from_dict = TvSeriesKeywords200Response.from_dict(tv_series_keywords200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


