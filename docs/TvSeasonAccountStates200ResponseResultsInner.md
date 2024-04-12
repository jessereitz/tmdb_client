# TvSeasonAccountStates200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**episode_number** | **int** |  | [optional] [default to 0]
**rated** | [**MovieAccountStates200ResponseRated**](MovieAccountStates200ResponseRated.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_account_states200_response_results_inner import TvSeasonAccountStates200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonAccountStates200ResponseResultsInner from a JSON string
tv_season_account_states200_response_results_inner_instance = TvSeasonAccountStates200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(TvSeasonAccountStates200ResponseResultsInner.to_json())

# convert the object into a dict
tv_season_account_states200_response_results_inner_dict = tv_season_account_states200_response_results_inner_instance.to_dict()
# create an instance of TvSeasonAccountStates200ResponseResultsInner from a dict
tv_season_account_states200_response_results_inner_from_dict = TvSeasonAccountStates200ResponseResultsInner.from_dict(tv_season_account_states200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


