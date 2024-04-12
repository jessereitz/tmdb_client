# TvSeriesTranslations200ResponseTranslationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_3166_1** | **str** |  | [optional] 
**iso_639_1** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**english_name** | **str** |  | [optional] 
**data** | [**TvSeriesTranslations200ResponseTranslationsInnerData**](TvSeriesTranslations200ResponseTranslationsInnerData.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_translations200_response_translations_inner import TvSeriesTranslations200ResponseTranslationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesTranslations200ResponseTranslationsInner from a JSON string
tv_series_translations200_response_translations_inner_instance = TvSeriesTranslations200ResponseTranslationsInner.from_json(json)
# print the JSON string representation of the object
print(TvSeriesTranslations200ResponseTranslationsInner.to_json())

# convert the object into a dict
tv_series_translations200_response_translations_inner_dict = tv_series_translations200_response_translations_inner_instance.to_dict()
# create an instance of TvSeriesTranslations200ResponseTranslationsInner from a dict
tv_series_translations200_response_translations_inner_from_dict = TvSeriesTranslations200ResponseTranslationsInner.from_dict(tv_series_translations200_response_translations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


