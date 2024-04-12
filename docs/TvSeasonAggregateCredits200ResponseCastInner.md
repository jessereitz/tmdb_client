# TvSeasonAggregateCredits200ResponseCastInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] [default to True]
**gender** | **int** |  | [optional] [default to 0]
**id** | **int** |  | [optional] [default to 0]
**known_for_department** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**original_name** | **str** |  | [optional] 
**popularity** | **float** |  | [optional] [default to 0]
**profile_path** | **str** |  | [optional] 
**roles** | [**List[TvSeasonAggregateCredits200ResponseCastInnerRolesInner]**](TvSeasonAggregateCredits200ResponseCastInnerRolesInner.md) |  | [optional] 
**total_episode_count** | **int** |  | [optional] [default to 0]
**order** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.tv_season_aggregate_credits200_response_cast_inner import TvSeasonAggregateCredits200ResponseCastInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonAggregateCredits200ResponseCastInner from a JSON string
tv_season_aggregate_credits200_response_cast_inner_instance = TvSeasonAggregateCredits200ResponseCastInner.from_json(json)
# print the JSON string representation of the object
print(TvSeasonAggregateCredits200ResponseCastInner.to_json())

# convert the object into a dict
tv_season_aggregate_credits200_response_cast_inner_dict = tv_season_aggregate_credits200_response_cast_inner_instance.to_dict()
# create an instance of TvSeasonAggregateCredits200ResponseCastInner from a dict
tv_season_aggregate_credits200_response_cast_inner_from_dict = TvSeasonAggregateCredits200ResponseCastInner.from_dict(tv_season_aggregate_credits200_response_cast_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


