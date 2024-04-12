# TvSeriesTranslations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**translations** | [**List[TvSeriesTranslations200ResponseTranslationsInner]**](TvSeriesTranslations200ResponseTranslationsInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_translations200_response import TvSeriesTranslations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesTranslations200Response from a JSON string
tv_series_translations200_response_instance = TvSeriesTranslations200Response.from_json(json)
# print the JSON string representation of the object
print(TvSeriesTranslations200Response.to_json())

# convert the object into a dict
tv_series_translations200_response_dict = tv_series_translations200_response_instance.to_dict()
# create an instance of TvSeriesTranslations200Response from a dict
tv_series_translations200_response_from_dict = TvSeriesTranslations200Response.from_dict(tv_series_translations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


