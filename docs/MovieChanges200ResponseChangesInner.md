# MovieChanges200ResponseChangesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**items** | [**List[MovieChanges200ResponseChangesInnerItemsInner]**](MovieChanges200ResponseChangesInnerItemsInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_changes200_response_changes_inner import MovieChanges200ResponseChangesInner

# TODO update the JSON string below
json = "{}"
# create an instance of MovieChanges200ResponseChangesInner from a JSON string
movie_changes200_response_changes_inner_instance = MovieChanges200ResponseChangesInner.from_json(json)
# print the JSON string representation of the object
print(MovieChanges200ResponseChangesInner.to_json())

# convert the object into a dict
movie_changes200_response_changes_inner_dict = movie_changes200_response_changes_inner_instance.to_dict()
# create an instance of MovieChanges200ResponseChangesInner from a dict
movie_changes200_response_changes_inner_from_dict = MovieChanges200ResponseChangesInner.from_dict(movie_changes200_response_changes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


