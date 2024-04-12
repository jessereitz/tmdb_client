# TvSeasonDetails200ResponseEpisodesInnerCrewInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**department** | **str** |  | [optional] 
**job** | **str** |  | [optional] 
**credit_id** | **str** |  | [optional] 
**adult** | **bool** |  | [optional] [default to True]
**gender** | **int** |  | [optional] [default to 0]
**id** | **int** |  | [optional] [default to 0]
**known_for_department** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**original_name** | **str** |  | [optional] 
**popularity** | **float** |  | [optional] [default to 0]
**profile_path** | **str** |  | [optional] 

## Example

```python
from tmdb_client.models.tv_season_details200_response_episodes_inner_crew_inner import TvSeasonDetails200ResponseEpisodesInnerCrewInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvSeasonDetails200ResponseEpisodesInnerCrewInner from a JSON string
tv_season_details200_response_episodes_inner_crew_inner_instance = TvSeasonDetails200ResponseEpisodesInnerCrewInner.from_json(json)
# print the JSON string representation of the object
print(TvSeasonDetails200ResponseEpisodesInnerCrewInner.to_json())

# convert the object into a dict
tv_season_details200_response_episodes_inner_crew_inner_dict = tv_season_details200_response_episodes_inner_crew_inner_instance.to_dict()
# create an instance of TvSeasonDetails200ResponseEpisodesInnerCrewInner from a dict
tv_season_details200_response_episodes_inner_crew_inner_from_dict = TvSeasonDetails200ResponseEpisodesInnerCrewInner.from_dict(tv_season_details200_response_episodes_inner_crew_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


