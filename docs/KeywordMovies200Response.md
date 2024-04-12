# KeywordMovies200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**page** | **int** |  | [optional] [default to 0]
**results** | [**List[KeywordMovies200ResponseResultsInner]**](KeywordMovies200ResponseResultsInner.md) |  | [optional] 
**total_pages** | **int** |  | [optional] [default to 0]
**total_results** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.keyword_movies200_response import KeywordMovies200Response

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordMovies200Response from a JSON string
keyword_movies200_response_instance = KeywordMovies200Response.from_json(json)
# print the JSON string representation of the object
print(KeywordMovies200Response.to_json())

# convert the object into a dict
keyword_movies200_response_dict = keyword_movies200_response_instance.to_dict()
# create an instance of KeywordMovies200Response from a dict
keyword_movies200_response_from_dict = KeywordMovies200Response.from_dict(keyword_movies200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


