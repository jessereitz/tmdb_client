# TvSeriesScreenedTheatrically200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**results** | [**List[TvSeriesScreenedTheatrically200ResponseResultsInner]**](TvSeriesScreenedTheatrically200ResponseResultsInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_screened_theatrically200_response import TvSeriesScreenedTheatrically200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesScreenedTheatrically200Response from a JSON string
tv_series_screened_theatrically200_response_instance = TvSeriesScreenedTheatrically200Response.from_json(json)
# print the JSON string representation of the object
print(TvSeriesScreenedTheatrically200Response.to_json())

# convert the object into a dict
tv_series_screened_theatrically200_response_dict = tv_series_screened_theatrically200_response_instance.to_dict()
# create an instance of TvSeriesScreenedTheatrically200Response from a dict
tv_series_screened_theatrically200_response_from_dict = TvSeriesScreenedTheatrically200Response.from_dict(tv_series_screened_theatrically200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


