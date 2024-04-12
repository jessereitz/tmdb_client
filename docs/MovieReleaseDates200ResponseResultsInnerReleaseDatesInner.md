# MovieReleaseDates200ResponseResultsInnerReleaseDatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certification** | **str** |  | [optional] 
**descriptors** | **List[str]** |  | [optional] 
**iso_639_1** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**release_date** | **str** |  | [optional] 
**type** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.movie_release_dates200_response_results_inner_release_dates_inner import MovieReleaseDates200ResponseResultsInnerReleaseDatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of MovieReleaseDates200ResponseResultsInnerReleaseDatesInner from a JSON string
movie_release_dates200_response_results_inner_release_dates_inner_instance = MovieReleaseDates200ResponseResultsInnerReleaseDatesInner.from_json(json)
# print the JSON string representation of the object
print(MovieReleaseDates200ResponseResultsInnerReleaseDatesInner.to_json())

# convert the object into a dict
movie_release_dates200_response_results_inner_release_dates_inner_dict = movie_release_dates200_response_results_inner_release_dates_inner_instance.to_dict()
# create an instance of MovieReleaseDates200ResponseResultsInnerReleaseDatesInner from a dict
movie_release_dates200_response_results_inner_release_dates_inner_from_dict = MovieReleaseDates200ResponseResultsInnerReleaseDatesInner.from_dict(movie_release_dates200_response_results_inner_release_dates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


