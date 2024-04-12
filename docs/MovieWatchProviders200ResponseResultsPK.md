# MovieWatchProviders200ResponseResultsPK


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsPKFlatrateInner]**](MovieWatchProviders200ResponseResultsPKFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_pk import MovieWatchProviders200ResponseResultsPK

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsPK from a JSON string
movie_watch_providers200_response_results_pk_instance = MovieWatchProviders200ResponseResultsPK.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsPK.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_pk_dict = movie_watch_providers200_response_results_pk_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsPK from a dict
movie_watch_providers200_response_results_pk_from_dict = MovieWatchProviders200ResponseResultsPK.from_dict(movie_watch_providers200_response_results_pk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


