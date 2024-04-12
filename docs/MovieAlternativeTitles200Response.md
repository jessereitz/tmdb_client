# MovieAlternativeTitles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**titles** | [**List[MovieAlternativeTitles200ResponseTitlesInner]**](MovieAlternativeTitles200ResponseTitlesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_alternative_titles200_response import MovieAlternativeTitles200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MovieAlternativeTitles200Response from a JSON string
movie_alternative_titles200_response_instance = MovieAlternativeTitles200Response.from_json(json)
# print the JSON string representation of the object
print(MovieAlternativeTitles200Response.to_json())

# convert the object into a dict
movie_alternative_titles200_response_dict = movie_alternative_titles200_response_instance.to_dict()
# create an instance of MovieAlternativeTitles200Response from a dict
movie_alternative_titles200_response_from_dict = MovieAlternativeTitles200Response.from_dict(movie_alternative_titles200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


