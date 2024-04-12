# MovieWatchProviders200ResponseResultsSE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsSEBuyInner]**](MovieWatchProviders200ResponseResultsSEBuyInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsSEBuyInner]**](MovieWatchProviders200ResponseResultsSEBuyInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsBEFlatrateInner]**](MovieWatchProviders200ResponseResultsBEFlatrateInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_se import MovieWatchProviders200ResponseResultsSE

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsSE from a JSON string
movie_watch_providers200_response_results_se_instance = MovieWatchProviders200ResponseResultsSE.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsSE.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_se_dict = movie_watch_providers200_response_results_se_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsSE from a dict
movie_watch_providers200_response_results_se_from_dict = MovieWatchProviders200ResponseResultsSE.from_dict(movie_watch_providers200_response_results_se_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


