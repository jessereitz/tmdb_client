# CertificationMovieList200ResponseCertificationsIDInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certification** | **str** |  | [optional] 
**meaning** | **str** |  | [optional] 
**order** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.certification_movie_list200_response_certifications_id_inner import CertificationMovieList200ResponseCertificationsIDInner

# TODO update the JSON string below
json = "{}"
# create an instance of CertificationMovieList200ResponseCertificationsIDInner from a JSON string
certification_movie_list200_response_certifications_id_inner_instance = CertificationMovieList200ResponseCertificationsIDInner.from_json(json)
# print the JSON string representation of the object
print(CertificationMovieList200ResponseCertificationsIDInner.to_json())

# convert the object into a dict
certification_movie_list200_response_certifications_id_inner_dict = certification_movie_list200_response_certifications_id_inner_instance.to_dict()
# create an instance of CertificationMovieList200ResponseCertificationsIDInner from a dict
certification_movie_list200_response_certifications_id_inner_from_dict = CertificationMovieList200ResponseCertificationsIDInner.from_dict(certification_movie_list200_response_certifications_id_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


