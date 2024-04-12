# ChangesPeopleList200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**adult** | **bool** |  | [optional] [default to True]

## Example

```python
from tmdb_client.models.changes_people_list200_response_results_inner import ChangesPeopleList200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChangesPeopleList200ResponseResultsInner from a JSON string
changes_people_list200_response_results_inner_instance = ChangesPeopleList200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(ChangesPeopleList200ResponseResultsInner.to_json())

# convert the object into a dict
changes_people_list200_response_results_inner_dict = changes_people_list200_response_results_inner_instance.to_dict()
# create an instance of ChangesPeopleList200ResponseResultsInner from a dict
changes_people_list200_response_results_inner_from_dict = ChangesPeopleList200ResponseResultsInner.from_dict(changes_people_list200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


