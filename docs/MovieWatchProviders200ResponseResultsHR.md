# MovieWatchProviders200ResponseResultsHR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsCOBuyInner]**](MovieWatchProviders200ResponseResultsCOBuyInner.md) |  | [optional] 
**ads** | [**List[MovieWatchProviders200ResponseResultsHRAdsInner]**](MovieWatchProviders200ResponseResultsHRAdsInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_hr import MovieWatchProviders200ResponseResultsHR

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsHR from a JSON string
movie_watch_providers200_response_results_hr_instance = MovieWatchProviders200ResponseResultsHR.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsHR.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_hr_dict = movie_watch_providers200_response_results_hr_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsHR from a dict
movie_watch_providers200_response_results_hr_from_dict = MovieWatchProviders200ResponseResultsHR.from_dict(movie_watch_providers200_response_results_hr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


