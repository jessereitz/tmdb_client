# CreditDetails200ResponseMediaSeasonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**air_date** | **str** |  | [optional] 
**episode_count** | **int** |  | [optional] [default to 0]
**id** | **int** |  | [optional] [default to 0]
**name** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**poster_path** | **str** |  | [optional] 
**season_number** | **int** |  | [optional] [default to 0]
**show_id** | **int** |  | [optional] [default to 0]

## Example

```python
from openapi_client.models.credit_details200_response_media_seasons_inner import CreditDetails200ResponseMediaSeasonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreditDetails200ResponseMediaSeasonsInner from a JSON string
credit_details200_response_media_seasons_inner_instance = CreditDetails200ResponseMediaSeasonsInner.from_json(json)
# print the JSON string representation of the object
print(CreditDetails200ResponseMediaSeasonsInner.to_json())

# convert the object into a dict
credit_details200_response_media_seasons_inner_dict = credit_details200_response_media_seasons_inner_instance.to_dict()
# create an instance of CreditDetails200ResponseMediaSeasonsInner from a dict
credit_details200_response_media_seasons_inner_from_dict = CreditDetails200ResponseMediaSeasonsInner.from_dict(credit_details200_response_media_seasons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


