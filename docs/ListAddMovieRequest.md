# ListAddMovieRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_body** | **str** |  | [optional] 

## Example

```python
from tmdb_client.models.list_add_movie_request import ListAddMovieRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListAddMovieRequest from a JSON string
list_add_movie_request_instance = ListAddMovieRequest.from_json(json)
# print the JSON string representation of the object
print(ListAddMovieRequest.to_json())

# convert the object into a dict
list_add_movie_request_dict = list_add_movie_request_instance.to_dict()
# create an instance of ListAddMovieRequest from a dict
list_add_movie_request_from_dict = ListAddMovieRequest.from_dict(list_add_movie_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


