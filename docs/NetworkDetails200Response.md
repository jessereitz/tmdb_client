# NetworkDetails200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headquarters** | **str** |  | [optional] 
**homepage** | **str** |  | [optional] 
**id** | **int** |  | [optional] [default to 0]
**logo_path** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**origin_country** | **str** |  | [optional] 

## Example

```python
from tmdb_client.models.network_details200_response import NetworkDetails200Response

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkDetails200Response from a JSON string
network_details200_response_instance = NetworkDetails200Response.from_json(json)
# print the JSON string representation of the object
print(NetworkDetails200Response.to_json())

# convert the object into a dict
network_details200_response_dict = network_details200_response_instance.to_dict()
# create an instance of NetworkDetails200Response from a dict
network_details200_response_from_dict = NetworkDetails200Response.from_dict(network_details200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


