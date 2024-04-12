# TvSeasonChangesById200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**List[TvSeasonChangesById200ResponseChangesInner]**](TvSeasonChangesById200ResponseChangesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.tv_season_changes_by_id200_response import TvSeasonChangesById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonChangesById200Response from a JSON string
tv_season_changes_by_id200_response_instance = TvSeasonChangesById200Response.from_json(json)
# print the JSON string representation of the object
print(TvSeasonChangesById200Response.to_json())

# convert the object into a dict
tv_season_changes_by_id200_response_dict = tv_season_changes_by_id200_response_instance.to_dict()
# create an instance of TvSeasonChangesById200Response from a dict
tv_season_changes_by_id200_response_from_dict = TvSeasonChangesById200Response.from_dict(tv_season_changes_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


