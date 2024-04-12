# PersonExternalIds200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**freebase_mid** | **str** |  | [optional] 
**freebase_id** | **str** |  | [optional] 
**imdb_id** | **str** |  | [optional] 
**tvrage_id** | **int** |  | [optional] [default to 0]
**wikidata_id** | **str** |  | [optional] 
**facebook_id** | **str** |  | [optional] 
**instagram_id** | **str** |  | [optional] 
**tiktok_id** | **str** |  | [optional] 
**twitter_id** | **str** |  | [optional] 
**youtube_id** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.person_external_ids200_response import PersonExternalIds200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PersonExternalIds200Response from a JSON string
person_external_ids200_response_instance = PersonExternalIds200Response.from_json(json)
# print the JSON string representation of the object
print(PersonExternalIds200Response.to_json())

# convert the object into a dict
person_external_ids200_response_dict = person_external_ids200_response_instance.to_dict()
# create an instance of PersonExternalIds200Response from a dict
person_external_ids200_response_from_dict = PersonExternalIds200Response.from_dict(person_external_ids200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


