# MovieImages200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backdrops** | [**List[MovieImages200ResponseBackdropsInner]**](MovieImages200ResponseBackdropsInner.md) |  | [optional] 
**id** | **int** |  | [optional] [default to 0]
**logos** | [**List[MovieImages200ResponseLogosInner]**](MovieImages200ResponseLogosInner.md) |  | [optional] 
**posters** | [**List[MovieImages200ResponsePostersInner]**](MovieImages200ResponsePostersInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_images200_response import MovieImages200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MovieImages200Response from a JSON string
movie_images200_response_instance = MovieImages200Response.from_json(json)
# print the JSON string representation of the object
print(MovieImages200Response.to_json())

# convert the object into a dict
movie_images200_response_dict = movie_images200_response_instance.to_dict()
# create an instance of MovieImages200Response from a dict
movie_images200_response_from_dict = MovieImages200Response.from_dict(movie_images200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


