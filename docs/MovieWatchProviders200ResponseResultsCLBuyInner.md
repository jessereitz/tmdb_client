# MovieWatchProviders200ResponseResultsCLBuyInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logo_path** | **str** |  | [optional] 
**provider_id** | **int** |  | [optional] [default to 0]
**provider_name** | **str** |  | [optional] 
**display_priority** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_cl_buy_inner import MovieWatchProviders200ResponseResultsCLBuyInner

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsCLBuyInner from a JSON string
movie_watch_providers200_response_results_cl_buy_inner_instance = MovieWatchProviders200ResponseResultsCLBuyInner.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsCLBuyInner.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_cl_buy_inner_dict = movie_watch_providers200_response_results_cl_buy_inner_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsCLBuyInner from a dict
movie_watch_providers200_response_results_cl_buy_inner_from_dict = MovieWatchProviders200ResponseResultsCLBuyInner.from_dict(movie_watch_providers200_response_results_cl_buy_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


