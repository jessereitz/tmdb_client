# MovieWatchProviders200ResponseResultsBR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsARFlatrateInner]**](MovieWatchProviders200ResponseResultsARFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_br import MovieWatchProviders200ResponseResultsBR

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsBR from a JSON string
movie_watch_providers200_response_results_br_instance = MovieWatchProviders200ResponseResultsBR.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsBR.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_br_dict = movie_watch_providers200_response_results_br_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsBR from a dict
movie_watch_providers200_response_results_br_from_dict = MovieWatchProviders200ResponseResultsBR.from_dict(movie_watch_providers200_response_results_br_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


