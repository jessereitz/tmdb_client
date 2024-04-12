# MovieWatchProviders200ResponseResultsAU


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsAUBuyInner]**](MovieWatchProviders200ResponseResultsAUBuyInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_au import MovieWatchProviders200ResponseResultsAU

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsAU from a JSON string
movie_watch_providers200_response_results_au_instance = MovieWatchProviders200ResponseResultsAU.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsAU.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_au_dict = movie_watch_providers200_response_results_au_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsAU from a dict
movie_watch_providers200_response_results_au_from_dict = MovieWatchProviders200ResponseResultsAU.from_dict(movie_watch_providers200_response_results_au_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


