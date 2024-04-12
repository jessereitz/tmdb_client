# TvSeriesAlternativeTitles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**results** | [**List[TvSeriesAlternativeTitles200ResponseResultsInner]**](TvSeriesAlternativeTitles200ResponseResultsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.tv_series_alternative_titles200_response import TvSeriesAlternativeTitles200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesAlternativeTitles200Response from a JSON string
tv_series_alternative_titles200_response_instance = TvSeriesAlternativeTitles200Response.from_json(json)
# print the JSON string representation of the object
print(TvSeriesAlternativeTitles200Response.to_json())

# convert the object into a dict
tv_series_alternative_titles200_response_dict = tv_series_alternative_titles200_response_instance.to_dict()
# create an instance of TvSeriesAlternativeTitles200Response from a dict
tv_series_alternative_titles200_response_from_dict = TvSeriesAlternativeTitles200Response.from_dict(tv_series_alternative_titles200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


