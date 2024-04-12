# CollectionTranslations200ResponseTranslationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_3166_1** | **str** |  | [optional] 
**iso_639_1** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**english_name** | **str** |  | [optional] 
**data** | [**CollectionTranslations200ResponseTranslationsInnerData**](CollectionTranslations200ResponseTranslationsInnerData.md) |  | [optional] 

## Example

```python
from openapi_client.models.collection_translations200_response_translations_inner import CollectionTranslations200ResponseTranslationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionTranslations200ResponseTranslationsInner from a JSON string
collection_translations200_response_translations_inner_instance = CollectionTranslations200ResponseTranslationsInner.from_json(json)
# print the JSON string representation of the object
print(CollectionTranslations200ResponseTranslationsInner.to_json())

# convert the object into a dict
collection_translations200_response_translations_inner_dict = collection_translations200_response_translations_inner_instance.to_dict()
# create an instance of CollectionTranslations200ResponseTranslationsInner from a dict
collection_translations200_response_translations_inner_from_dict = CollectionTranslations200ResponseTranslationsInner.from_dict(collection_translations200_response_translations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


