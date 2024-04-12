# ChangesTvList200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [default to 0]
**adult** | **bool** |  | [optional] [default to True]

## Example

```python
from tmdb_client.models.changes_tv_list200_response_results_inner import ChangesTvList200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChangesTvList200ResponseResultsInner from a JSON string
changes_tv_list200_response_results_inner_instance = ChangesTvList200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(ChangesTvList200ResponseResultsInner.to_json())

# convert the object into a dict
changes_tv_list200_response_results_inner_dict = changes_tv_list200_response_results_inner_instance.to_dict()
# create an instance of ChangesTvList200ResponseResultsInner from a dict
changes_tv_list200_response_results_inner_from_dict = ChangesTvList200ResponseResultsInner.from_dict(changes_tv_list200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


