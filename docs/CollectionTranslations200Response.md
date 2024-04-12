# CollectionTranslations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**translations** | [**List[CollectionTranslations200ResponseTranslationsInner]**](CollectionTranslations200ResponseTranslationsInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.collection_translations200_response import CollectionTranslations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionTranslations200Response from a JSON string
collection_translations200_response_instance = CollectionTranslations200Response.from_json(json)
# print the JSON string representation of the object
print(CollectionTranslations200Response.to_json())

# convert the object into a dict
collection_translations200_response_dict = collection_translations200_response_instance.to_dict()
# create an instance of CollectionTranslations200Response from a dict
collection_translations200_response_from_dict = CollectionTranslations200Response.from_dict(collection_translations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


