# TvEpisodeDetails200ResponseCrewInner


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
from openapi_client.models.tv_episode_details200_response_crew_inner import TvEpisodeDetails200ResponseCrewInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvEpisodeDetails200ResponseCrewInner from a JSON string
tv_episode_details200_response_crew_inner_instance = TvEpisodeDetails200ResponseCrewInner.from_json(json)
# print the JSON string representation of the object
print(TvEpisodeDetails200ResponseCrewInner.to_json())

# convert the object into a dict
tv_episode_details200_response_crew_inner_dict = tv_episode_details200_response_crew_inner_instance.to_dict()
# create an instance of TvEpisodeDetails200ResponseCrewInner from a dict
tv_episode_details200_response_crew_inner_from_dict = TvEpisodeDetails200ResponseCrewInner.from_dict(tv_episode_details200_response_crew_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


