# CertificationMovieList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certifications** | [**CertificationMovieList200ResponseCertifications**](CertificationMovieList200ResponseCertifications.md) |  | [optional] 

## Example

```python
from tmdb_client.models.certification_movie_list200_response import CertificationMovieList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CertificationMovieList200Response from a JSON string
certification_movie_list200_response_instance = CertificationMovieList200Response.from_json(json)
# print the JSON string representation of the object
print(CertificationMovieList200Response.to_json())

# convert the object into a dict
certification_movie_list200_response_dict = certification_movie_list200_response_instance.to_dict()
# create an instance of CertificationMovieList200Response from a dict
certification_movie_list200_response_from_dict = CertificationMovieList200Response.from_dict(certification_movie_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


