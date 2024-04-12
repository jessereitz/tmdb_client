# MovieTranslations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**translations** | [**List[MovieTranslations200ResponseTranslationsInner]**](MovieTranslations200ResponseTranslationsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_translations200_response import MovieTranslations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MovieTranslations200Response from a JSON string
movie_translations200_response_instance = MovieTranslations200Response.from_json(json)
# print the JSON string representation of the object
print(MovieTranslations200Response.to_json())

# convert the object into a dict
movie_translations200_response_dict = movie_translations200_response_instance.to_dict()
# create an instance of MovieTranslations200Response from a dict
movie_translations200_response_from_dict = MovieTranslations200Response.from_dict(movie_translations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


