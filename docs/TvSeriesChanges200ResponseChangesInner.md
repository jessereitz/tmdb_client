# TvSeriesChanges200ResponseChangesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**items** | [**List[TvSeriesChanges200ResponseChangesInnerItemsInner]**](TvSeriesChanges200ResponseChangesInnerItemsInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_series_changes200_response_changes_inner import TvSeriesChanges200ResponseChangesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeriesChanges200ResponseChangesInner from a JSON string
tv_series_changes200_response_changes_inner_instance = TvSeriesChanges200ResponseChangesInner.from_json(json)
# print the JSON string representation of the object
print(TvSeriesChanges200ResponseChangesInner.to_json())

# convert the object into a dict
tv_series_changes200_response_changes_inner_dict = tv_series_changes200_response_changes_inner_instance.to_dict()
# create an instance of TvSeriesChanges200ResponseChangesInner from a dict
tv_series_changes200_response_changes_inner_from_dict = TvSeriesChanges200ResponseChangesInner.from_dict(tv_series_changes200_response_changes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


