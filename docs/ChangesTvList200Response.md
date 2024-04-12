# ChangesTvList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ChangesTvList200ResponseResultsInner]**](ChangesTvList200ResponseResultsInner.md) |  | [optional] 
**page** | **int** |  | [optional] [default to 0]
**total_pages** | **int** |  | [optional] [default to 0]
**total_results** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.changes_tv_list200_response import ChangesTvList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ChangesTvList200Response from a JSON string
changes_tv_list200_response_instance = ChangesTvList200Response.from_json(json)
# print the JSON string representation of the object
print(ChangesTvList200Response.to_json())

# convert the object into a dict
changes_tv_list200_response_dict = changes_tv_list200_response_instance.to_dict()
# create an instance of ChangesTvList200Response from a dict
changes_tv_list200_response_from_dict = ChangesTvList200Response.from_dict(changes_tv_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


