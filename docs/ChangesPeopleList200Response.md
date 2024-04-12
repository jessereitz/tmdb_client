# ChangesPeopleList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ChangesPeopleList200ResponseResultsInner]**](ChangesPeopleList200ResponseResultsInner.md) |  | [optional] 
**page** | **int** |  | [optional] [default to 0]
**total_pages** | **int** |  | [optional] [default to 0]
**total_results** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.changes_people_list200_response import ChangesPeopleList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ChangesPeopleList200Response from a JSON string
changes_people_list200_response_instance = ChangesPeopleList200Response.from_json(json)
# print the JSON string representation of the object
print(ChangesPeopleList200Response.to_json())

# convert the object into a dict
changes_people_list200_response_dict = changes_people_list200_response_instance.to_dict()
# create an instance of ChangesPeopleList200Response from a dict
changes_people_list200_response_from_dict = ChangesPeopleList200Response.from_dict(changes_people_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


