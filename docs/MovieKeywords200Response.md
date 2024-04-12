# MovieKeywords200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**keywords** | [**List[MovieKeywords200ResponseKeywordsInner]**](MovieKeywords200ResponseKeywordsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_keywords200_response import MovieKeywords200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MovieKeywords200Response from a JSON string
movie_keywords200_response_instance = MovieKeywords200Response.from_json(json)
# print the JSON string representation of the object
print(MovieKeywords200Response.to_json())

# convert the object into a dict
movie_keywords200_response_dict = movie_keywords200_response_instance.to_dict()
# create an instance of MovieKeywords200Response from a dict
movie_keywords200_response_from_dict = MovieKeywords200Response.from_dict(movie_keywords200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


