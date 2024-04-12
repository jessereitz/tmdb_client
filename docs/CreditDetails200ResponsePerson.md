# CreditDetails200ResponsePerson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] [default to True]
**id** | **int** |  | [optional] [default to 0]
**name** | **str** |  | [optional] 
**original_name** | **str** |  | [optional] 
**media_type** | **str** |  | [optional] 
**popularity** | **float** |  | [optional] [default to 0]
**gender** | **int** |  | [optional] [default to 0]
**known_for_department** | **str** |  | [optional] 
**profile_path** | **str** |  | [optional] 

## Example

```python
from tmdb_client.models.credit_details200_response_person import CreditDetails200ResponsePerson

# TODO update the JSON string below
json = "{}"
# create an instance of CreditDetails200ResponsePerson from a JSON string
credit_details200_response_person_instance = CreditDetails200ResponsePerson.from_json(json)
# print the JSON string representation of the object
print(CreditDetails200ResponsePerson.to_json())

# convert the object into a dict
credit_details200_response_person_dict = credit_details200_response_person_instance.to_dict()
# create an instance of CreditDetails200ResponsePerson from a dict
credit_details200_response_person_from_dict = CreditDetails200ResponsePerson.from_dict(credit_details200_response_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


