# KeywordDetails200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**name** | **str** |  | [optional] 

## Example

```python
from tmdb_client.models.keyword_details200_response import KeywordDetails200Response

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordDetails200Response from a JSON string
keyword_details200_response_instance = KeywordDetails200Response.from_json(json)
# print the JSON string representation of the object
print(KeywordDetails200Response.to_json())

# convert the object into a dict
keyword_details200_response_dict = keyword_details200_response_instance.to_dict()
# create an instance of KeywordDetails200Response from a dict
keyword_details200_response_from_dict = KeywordDetails200Response.from_dict(keyword_details200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


