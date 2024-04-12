# TvEpisodeChangesById200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**List[TvEpisodeChangesById200ResponseChangesInner]**](TvEpisodeChangesById200ResponseChangesInner.md) |  | [optional] 

## Example

```python
from tmdb_client.models.tv_episode_changes_by_id200_response import TvEpisodeChangesById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TvEpisodeChangesById200Response from a JSON string
tv_episode_changes_by_id200_response_instance = TvEpisodeChangesById200Response.from_json(json)
# print the JSON string representation of the object
print(TvEpisodeChangesById200Response.to_json())

# convert the object into a dict
tv_episode_changes_by_id200_response_dict = tv_episode_changes_by_id200_response_instance.to_dict()
# create an instance of TvEpisodeChangesById200Response from a dict
tv_episode_changes_by_id200_response_from_dict = TvEpisodeChangesById200Response.from_dict(tv_episode_changes_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


