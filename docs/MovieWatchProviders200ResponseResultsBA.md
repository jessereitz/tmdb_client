# MovieWatchProviders200ResponseResultsBA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsALBuyInner]**](MovieWatchProviders200ResponseResultsALBuyInner.md) |  | [optional] 
**flatrate** | [**List[MovieWatchProviders200ResponseResultsAUFlatrateInner]**](MovieWatchProviders200ResponseResultsAUFlatrateInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_ba import MovieWatchProviders200ResponseResultsBA

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsBA from a JSON string
movie_watch_providers200_response_results_ba_instance = MovieWatchProviders200ResponseResultsBA.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsBA.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_ba_dict = movie_watch_providers200_response_results_ba_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsBA from a dict
movie_watch_providers200_response_results_ba_from_dict = MovieWatchProviders200ResponseResultsBA.from_dict(movie_watch_providers200_response_results_ba_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


