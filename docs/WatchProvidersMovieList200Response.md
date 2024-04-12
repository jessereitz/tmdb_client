# WatchProvidersMovieList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[WatchProvidersMovieList200ResponseResultsInner]**](WatchProvidersMovieList200ResponseResultsInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.watch_providers_movie_list200_response import WatchProvidersMovieList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of WatchProvidersMovieList200Response from a JSON string
watch_providers_movie_list200_response_instance = WatchProvidersMovieList200Response.from_json(json)
# print the JSON string representation of the object
print(WatchProvidersMovieList200Response.to_json())

# convert the object into a dict
watch_providers_movie_list200_response_dict = watch_providers_movie_list200_response_instance.to_dict()
# create an instance of WatchProvidersMovieList200Response from a dict
watch_providers_movie_list200_response_from_dict = WatchProvidersMovieList200Response.from_dict(watch_providers_movie_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


