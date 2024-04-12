# MovieChanges200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**List[MovieChanges200ResponseChangesInner]**](MovieChanges200ResponseChangesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_changes200_response import MovieChanges200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MovieChanges200Response from a JSON string
movie_changes200_response_instance = MovieChanges200Response.from_json(json)
# print the JSON string representation of the object
print(MovieChanges200Response.to_json())

# convert the object into a dict
movie_changes200_response_dict = movie_changes200_response_instance.to_dict()
# create an instance of MovieChanges200Response from a dict
movie_changes200_response_from_dict = MovieChanges200Response.from_dict(movie_changes200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


