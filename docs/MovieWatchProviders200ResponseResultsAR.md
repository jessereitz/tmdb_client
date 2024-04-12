# MovieWatchProviders200ResponseResultsAR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsARBuyInner]**](MovieWatchProviders200ResponseResultsARBuyInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsARFlatrateInner]**](MovieWatchProviders200ResponseResultsARFlatrateInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsARBuyInner]**](MovieWatchProviders200ResponseResultsARBuyInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_ar import MovieWatchProviders200ResponseResultsAR

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsAR from a JSON string
movie_watch_providers200_response_results_ar_instance = MovieWatchProviders200ResponseResultsAR.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsAR.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_ar_dict = movie_watch_providers200_response_results_ar_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsAR from a dict
movie_watch_providers200_response_results_ar_from_dict = MovieWatchProviders200ResponseResultsAR.from_dict(movie_watch_providers200_response_results_ar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


