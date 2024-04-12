# TvSeasonTranslations200ResponseTranslationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_3166_1** | **str** |  | [optional] 
**iso_639_1** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**english_name** | **str** |  | [optional] 
**data** | [**TvSeasonTranslations200ResponseTranslationsInnerData**](TvSeasonTranslations200ResponseTranslationsInnerData.md) |  | [optional] 

## Example

```python
from openapi_client.models.tv_season_translations200_response_translations_inner import TvSeasonTranslations200ResponseTranslationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonTranslations200ResponseTranslationsInner from a JSON string
tv_season_translations200_response_translations_inner_instance = TvSeasonTranslations200ResponseTranslationsInner.from_json(json)
# print the JSON string representation of the object
print(TvSeasonTranslations200ResponseTranslationsInner.to_json())

# convert the object into a dict
tv_season_translations200_response_translations_inner_dict = tv_season_translations200_response_translations_inner_instance.to_dict()
# create an instance of TvSeasonTranslations200ResponseTranslationsInner from a dict
tv_season_translations200_response_translations_inner_from_dict = TvSeasonTranslations200ResponseTranslationsInner.from_dict(tv_season_translations200_response_translations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


