# TvSeriesChanges200ResponseChangesInnerItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**action** | **str** |  | [optional] 
**time** | **str** |  | [optional] 
**iso_639_1** | **str** |  | [optional] 
**iso_3166_1** | **str** |  | [optional] 
**value** | [**TvSeriesChanges200ResponseChangesInnerItemsInnerValue**](TvSeriesChanges200ResponseChangesInnerItemsInnerValue.md) |  | [optional] 
**original_value** | [**TvSeriesChanges200ResponseChangesInnerItemsInnerOriginalValue**](TvSeriesChanges200ResponseChangesInnerItemsInnerOriginalValue.md) |  | [optional] 

## Example

```python
from openapi_client.models.tv_series_changes200_response_changes_inner_items_inner import TvSeriesChanges200ResponseChangesInnerItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesChanges200ResponseChangesInnerItemsInner from a JSON string
tv_series_changes200_response_changes_inner_items_inner_instance = TvSeriesChanges200ResponseChangesInnerItemsInner.from_json(json)
# print the JSON string representation of the object
print(TvSeriesChanges200ResponseChangesInnerItemsInner.to_json())

# convert the object into a dict
tv_series_changes200_response_changes_inner_items_inner_dict = tv_series_changes200_response_changes_inner_items_inner_instance.to_dict()
# create an instance of TvSeriesChanges200ResponseChangesInnerItemsInner from a dict
tv_series_changes200_response_changes_inner_items_inner_from_dict = TvSeriesChanges200ResponseChangesInnerItemsInner.from_dict(tv_series_changes200_response_changes_inner_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


