# TvSeriesReviews200ResponseResultsInnerAuthorDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**avatar_path** | **str** |  | [optional] 
**rating** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.tv_series_reviews200_response_results_inner_author_details import TvSeriesReviews200ResponseResultsInnerAuthorDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesReviews200ResponseResultsInnerAuthorDetails from a JSON string
tv_series_reviews200_response_results_inner_author_details_instance = TvSeriesReviews200ResponseResultsInnerAuthorDetails.from_json(json)
# print the JSON string representation of the object
print(TvSeriesReviews200ResponseResultsInnerAuthorDetails.to_json())

# convert the object into a dict
tv_series_reviews200_response_results_inner_author_details_dict = tv_series_reviews200_response_results_inner_author_details_instance.to_dict()
# create an instance of TvSeriesReviews200ResponseResultsInnerAuthorDetails from a dict
tv_series_reviews200_response_results_inner_author_details_from_dict = TvSeriesReviews200ResponseResultsInnerAuthorDetails.from_dict(tv_series_reviews200_response_results_inner_author_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


