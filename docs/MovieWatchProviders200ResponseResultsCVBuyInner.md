# MovieWatchProviders200ResponseResultsCVBuyInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logo_path** | **str** |  | [optional] 
**provider_id** | **int** |  | [optional] [default to 0]
**provider_name** | **str** |  | [optional] 
**display_priority** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.movie_watch_providers200_response_results_cv_buy_inner import MovieWatchProviders200ResponseResultsCVBuyInner

# TODO update the JSON string below
json = "{}"
# create an instance of MovieWatchProviders200ResponseResultsCVBuyInner from a JSON string
movie_watch_providers200_response_results_cv_buy_inner_instance = MovieWatchProviders200ResponseResultsCVBuyInner.from_json(json)
# print the JSON string representation of the object
print(MovieWatchProviders200ResponseResultsCVBuyInner.to_json())

# convert the object into a dict
movie_watch_providers200_response_results_cv_buy_inner_dict = movie_watch_providers200_response_results_cv_buy_inner_instance.to_dict()
# create an instance of MovieWatchProviders200ResponseResultsCVBuyInner from a dict
movie_watch_providers200_response_results_cv_buy_inner_from_dict = MovieWatchProviders200ResponseResultsCVBuyInner.from_dict(movie_watch_providers200_response_results_cv_buy_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


