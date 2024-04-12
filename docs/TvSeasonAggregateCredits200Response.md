# TvSeasonAggregateCredits200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cast** | [**List[TvSeasonAggregateCredits200ResponseCastInner]**](TvSeasonAggregateCredits200ResponseCastInner.md) |  | [optional] 
**crew** | [**List[TvSeasonAggregateCredits200ResponseCrewInner]**](TvSeasonAggregateCredits200ResponseCrewInner.md) |  | [optional] 
**id** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.tv_season_aggregate_credits200_response import TvSeasonAggregateCredits200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonAggregateCredits200Response from a JSON string
tv_season_aggregate_credits200_response_instance = TvSeasonAggregateCredits200Response.from_json(json)
# print the JSON string representation of the object
print(TvSeasonAggregateCredits200Response.to_json())

# convert the object into a dict
tv_season_aggregate_credits200_response_dict = tv_season_aggregate_credits200_response_instance.to_dict()
# create an instance of TvSeasonAggregateCredits200Response from a dict
tv_season_aggregate_credits200_response_from_dict = TvSeasonAggregateCredits200Response.from_dict(tv_season_aggregate_credits200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


