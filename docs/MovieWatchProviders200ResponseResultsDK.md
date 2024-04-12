# MovieWatchProviders200ResponseResultsDK


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsDKRentInner]**](MovieWatchProviders200ResponseResultsDKRentInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsBEFlatrateInner]**](MovieWatchProviders200ResponseResultsBEFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsDKRentInner]**](MovieWatchProviders200ResponseResultsDKRentInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_dk import MovieWatchProviders200ResponseResultsDK

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsDK from a JSON string
movie_watch_providers200_response_results_dk_instance = MovieWatchProviders200ResponseResultsDK.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsDK.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_dk_dict = movie_watch_providers200_response_results_dk_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsDK from a dict
movie_watch_providers200_response_results_dk_from_dict = MovieWatchProviders200ResponseResultsDK.from_dict(movie_watch_providers200_response_results_dk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


