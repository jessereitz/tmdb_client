# CreditDetails200ResponseMedia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult** | **bool** |  | [optional] [default to True]
**backdrop_path** | **str** |  | [optional] 
**id** | **int** |  | [optional] [default to 0]
**name** | **str** |  | [optional] 
**original_language** | **str** |  | [optional] 
**original_name** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**poster_path** | **str** |  | [optional] 
**media_type** | **str** |  | [optional] 
**genre_ids** | **List[int]** |  | [optional] 
**popularity** | **float** |  | [optional] [default to 0]
**first_air_date** | **str** |  | [optional] 
**vote_average** | **float** |  | [optional] [default to 0]
**vote_count** | **int** |  | [optional] [default to 0]
**origin_country** | **List[str]** |  | [optional] 
**character** | **str** |  | [optional] 
**episodes** | **List[str]** |  | [optional] 
**seasons** | [**List[CreditDetails200ResponseMediaSeasonsInner]**](CreditDetails200ResponseMediaSeasonsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.credit_details200_response_media import CreditDetails200ResponseMedia

# TODO update the JSON string below
json = "{}"
# create an instance of CreditDetails200ResponseMedia from a JSON string
credit_details200_response_media_instance = CreditDetails200ResponseMedia.from_json(json)
# print the JSON string representation of the object
print(CreditDetails200ResponseMedia.to_json())

# convert the object into a dict
credit_details200_response_media_dict = credit_details200_response_media_instance.to_dict()
# create an instance of CreditDetails200ResponseMedia from a dict
credit_details200_response_media_from_dict = CreditDetails200ResponseMedia.from_dict(credit_details200_response_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


