# TvSeriesChanges200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**List[TvSeriesChanges200ResponseChangesInner]**](TvSeriesChanges200ResponseChangesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.tv_series_changes200_response import TvSeriesChanges200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesChanges200Response from a JSON string
tv_series_changes200_response_instance = TvSeriesChanges200Response.from_json(json)
# print the JSON string representation of the object
print(TvSeriesChanges200Response.to_json())

# convert the object into a dict
tv_series_changes200_response_dict = tv_series_changes200_response_instance.to_dict()
# create an instance of TvSeriesChanges200Response from a dict
tv_series_changes200_response_from_dict = TvSeriesChanges200Response.from_dict(tv_series_changes200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


