# PersonPopularList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] [default to 0]
**results** | [**List[PersonPopularList200ResponseResultsInner]**](PersonPopularList200ResponseResultsInner.md) |  | [optional] 
**total_pages** | **int** |  | [optional] [default to 0]
**total_results** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.person_popular_list200_response import PersonPopularList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PersonPopularList200Response from a JSON string
person_popular_list200_response_instance = PersonPopularList200Response.from_json(json)
# print the JSON string representation of the object
print(PersonPopularList200Response.to_json())

# convert the object into a dict
person_popular_list200_response_dict = person_popular_list200_response_instance.to_dict()
# create an instance of PersonPopularList200Response from a dict
person_popular_list200_response_from_dict = PersonPopularList200Response.from_dict(person_popular_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


