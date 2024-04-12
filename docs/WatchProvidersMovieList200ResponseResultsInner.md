# WatchProvidersMovieList200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_priorities** | [**WatchProvidersMovieList200ResponseResultsInnerDisplayPriorities**](WatchProvidersMovieList200ResponseResultsInnerDisplayPriorities.md) |  | [optional] 
**display_priority** | **int** |  | [optional] [default to 0]
**logo_path** | **str** |  | [optional] 
**provider_name** | **str** |  | [optional] 
**provider_id** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.watch_providers_movie_list200_response_results_inner import WatchProvidersMovieList200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of WatchProvidersMovieList200ResponseResultsInner from a JSON string
watch_providers_movie_list200_response_results_inner_instance = WatchProvidersMovieList200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(WatchProvidersMovieList200ResponseResultsInner.to_json())

# convert the object into a dict
watch_providers_movie_list200_response_results_inner_dict = watch_providers_movie_list200_response_results_inner_instance.to_dict()
# create an instance of WatchProvidersMovieList200ResponseResultsInner from a dict
watch_providers_movie_list200_response_results_inner_from_dict = WatchProvidersMovieList200ResponseResultsInner.from_dict(watch_providers_movie_list200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


