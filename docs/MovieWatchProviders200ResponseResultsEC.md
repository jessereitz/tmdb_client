# MovieWatchProviders200ResponseResultsEC


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsECBuyInner]**](MovieWatchProviders200ResponseResultsECBuyInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsARFlatrateInner]**](MovieWatchProviders200ResponseResultsARFlatrateInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsECBuyInner]**](MovieWatchProviders200ResponseResultsECBuyInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_ec import MovieWatchProviders200ResponseResultsEC

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsEC from a JSON string
movie_watch_providers200_response_results_ec_instance = MovieWatchProviders200ResponseResultsEC.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsEC.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_ec_dict = movie_watch_providers200_response_results_ec_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsEC from a dict
movie_watch_providers200_response_results_ec_from_dict = MovieWatchProviders200ResponseResultsEC.from_dict(movie_watch_providers200_response_results_ec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


