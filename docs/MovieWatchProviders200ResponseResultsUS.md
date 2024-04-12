# MovieWatchProviders200ResponseResultsUS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsUSRentInner]**](MovieWatchProviders200ResponseResultsUSRentInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsUSFlatrateInner]**](MovieWatchProviders200ResponseResultsUSFlatrateInner.md) |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsDEBuyInner]**](MovieWatchProviders200ResponseResultsDEBuyInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_us import MovieWatchProviders200ResponseResultsUS

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsUS from a JSON string
movie_watch_providers200_response_results_us_instance = MovieWatchProviders200ResponseResultsUS.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsUS.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_us_dict = movie_watch_providers200_response_results_us_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsUS from a dict
movie_watch_providers200_response_results_us_from_dict = MovieWatchProviders200ResponseResultsUS.from_dict(movie_watch_providers200_response_results_us_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


