# MovieWatchProviders200ResponseResultsCV


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsCVBuyInner]**](MovieWatchProviders200ResponseResultsCVBuyInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsCVBuyInner]**](MovieWatchProviders200ResponseResultsCVBuyInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_cv import MovieWatchProviders200ResponseResultsCV

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsCV from a JSON string
movie_watch_providers200_response_results_cv_instance = MovieWatchProviders200ResponseResultsCV.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsCV.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_cv_dict = movie_watch_providers200_response_results_cv_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsCV from a dict
movie_watch_providers200_response_results_cv_from_dict = MovieWatchProviders200ResponseResultsCV.from_dict(movie_watch_providers200_response_results_cv_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


