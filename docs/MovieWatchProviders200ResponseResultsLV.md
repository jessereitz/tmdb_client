# MovieWatchProviders200ResponseResultsLV


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsCZBuyInner]**](MovieWatchProviders200ResponseResultsCZBuyInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_lv import MovieWatchProviders200ResponseResultsLV

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsLV from a JSON string
movie_watch_providers200_response_results_lv_instance = MovieWatchProviders200ResponseResultsLV.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsLV.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_lv_dict = movie_watch_providers200_response_results_lv_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsLV from a dict
movie_watch_providers200_response_results_lv_from_dict = MovieWatchProviders200ResponseResultsLV.from_dict(movie_watch_providers200_response_results_lv_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


