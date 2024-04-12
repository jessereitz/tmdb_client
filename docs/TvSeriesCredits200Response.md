# TvSeriesCredits200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cast** | [**List[TvSeriesCredits200ResponseCastInner]**](TvSeriesCredits200ResponseCastInner.md) |  | [optional] 
**crew** | [**List[TvSeriesCredits200ResponseCrewInner]**](TvSeriesCredits200ResponseCrewInner.md) |  | [optional] 
**id** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.tv_series_credits200_response import TvSeriesCredits200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesCredits200Response from a JSON string
tv_series_credits200_response_instance = TvSeriesCredits200Response.from_json(json)
# print the JSON string representation of the object
print(TvSeriesCredits200Response.to_json())

# convert the object into a dict
tv_series_credits200_response_dict = tv_series_credits200_response_instance.to_dict()
# create an instance of TvSeriesCredits200Response from a dict
tv_series_credits200_response_from_dict = TvSeriesCredits200Response.from_dict(tv_series_credits200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


