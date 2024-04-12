# Translations200ResponseTranslationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_3166_1** | **str** |  | [optional] 
**iso_639_1** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**english_name** | **str** |  | [optional] 
**data** | [**Translations200ResponseTranslationsInnerData**](Translations200ResponseTranslationsInnerData.md) |  | [optional] 

## Example

```python
from tmdb_client.models.translations200_response_translations_inner import Translations200ResponseTranslationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of Translations200ResponseTranslationsInner from a JSON string
translations200_response_translations_inner_instance = Translations200ResponseTranslationsInner.from_json(json)
# print the JSON string representation of the object
print(Translations200ResponseTranslationsInner.to_json())

# convert the object into a dict
translations200_response_translations_inner_dict = translations200_response_translations_inner_instance.to_dict()
# create an instance of Translations200ResponseTranslationsInner from a dict
translations200_response_translations_inner_from_dict = Translations200ResponseTranslationsInner.from_dict(translations200_response_translations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


