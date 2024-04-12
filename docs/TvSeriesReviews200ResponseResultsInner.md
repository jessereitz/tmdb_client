# TvSeriesReviews200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | **str** |  | [optional] 
**author_details** | [**TvSeriesReviews200ResponseResultsInnerAuthorDetails**](TvSeriesReviews200ResponseResultsInnerAuthorDetails.md) |  | [optional] 
**content** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tv_series_reviews200_response_results_inner import TvSeriesReviews200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesReviews200ResponseResultsInner from a JSON string
tv_series_reviews200_response_results_inner_instance = TvSeriesReviews200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(TvSeriesReviews200ResponseResultsInner.to_json())

# convert the object into a dict
tv_series_reviews200_response_results_inner_dict = tv_series_reviews200_response_results_inner_instance.to_dict()
# create an instance of TvSeriesReviews200ResponseResultsInner from a dict
tv_series_reviews200_response_results_inner_from_dict = TvSeriesReviews200ResponseResultsInner.from_dict(tv_series_reviews200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


