# TvSeasonChangesById200ResponseChangesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**items** | [**List[TvSeasonChangesById200ResponseChangesInnerItemsInner]**](TvSeasonChangesById200ResponseChangesInnerItemsInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_changes_by_id200_response_changes_inner import TvSeasonChangesById200ResponseChangesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonChangesById200ResponseChangesInner from a JSON string
tv_season_changes_by_id200_response_changes_inner_instance = TvSeasonChangesById200ResponseChangesInner.from_json(json)
# print the JSON string representation of the object
print(TvSeasonChangesById200ResponseChangesInner.to_json())

# convert the object into a dict
tv_season_changes_by_id200_response_changes_inner_dict = tv_season_changes_by_id200_response_changes_inner_instance.to_dict()
# create an instance of TvSeasonChangesById200ResponseChangesInner from a dict
tv_season_changes_by_id200_response_changes_inner_from_dict = TvSeasonChangesById200ResponseChangesInner.from_dict(tv_season_changes_by_id200_response_changes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


