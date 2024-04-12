# MovieWatchProviders200ResponseResultsMU


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**buy** | [**List[MovieWatchProviders200ResponseResultsMUBuyInner]**](MovieWatchProviders200ResponseResultsMUBuyInner.md) |  | [optional] 
**rent** | [**List[MovieWatchProviders200ResponseResultsMUBuyInner]**](MovieWatchProviders200ResponseResultsMUBuyInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.movie_watch_providers200_response_results_mu import MovieWatchProviders200ResponseResultsMU

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsMU from a JSON string
movie_watch_providers200_response_results_mu_instance = MovieWatchProviders200ResponseResultsMU.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsMU.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_mu_dict = movie_watch_providers200_response_results_mu_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsMU from a dict
movie_watch_providers200_response_results_mu_from_dict = MovieWatchProviders200ResponseResultsMU.from_dict(movie_watch_providers200_response_results_mu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


