# TvSeriesDetails200ResponseCreatedByInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**credit_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**gender** | **int** |  | [optional] [default to 0]
**profile_path** | **str** |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_details200_response_created_by_inner import TvSeriesDetails200ResponseCreatedByInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesDetails200ResponseCreatedByInner from a JSON string
tv_series_details200_response_created_by_inner_instance = TvSeriesDetails200ResponseCreatedByInner.from_json(json)
# print the JSON string representation of the object
print(TvSeriesDetails200ResponseCreatedByInner.to_json())

# convert the object into a dict
tv_series_details200_response_created_by_inner_dict = tv_series_details200_response_created_by_inner_instance.to_dict()
# create an instance of TvSeriesDetails200ResponseCreatedByInner from a dict
tv_series_details200_response_created_by_inner_from_dict = TvSeriesDetails200ResponseCreatedByInner.from_dict(tv_series_details200_response_created_by_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


