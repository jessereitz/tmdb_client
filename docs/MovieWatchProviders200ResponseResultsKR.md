# MovieWatchProviders200ResponseResultsKR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsKRBuyInner]**](MovieWatchProviders200ResponseResultsKRBuyInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_kr import MovieWatchProviders200ResponseResultsKR

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsKR from a JSON string
movie_watch_providers200_response_results_kr_instance = MovieWatchProviders200ResponseResultsKR.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsKR.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_kr_dict = movie_watch_providers200_response_results_kr_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsKR from a dict
movie_watch_providers200_response_results_kr_from_dict = MovieWatchProviders200ResponseResultsKR.from_dict(movie_watch_providers200_response_results_kr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


