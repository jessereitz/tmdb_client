# CertificationMovieList200ResponseCertificationsARInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certification** | **str** |  | [optional] 
**meaning** | **str** |  | [optional] 
**order** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.certification_movie_list200_response_certifications_ar_inner import CertificationMovieList200ResponseCertificationsARInner

# TODO update the JSON string below
json = "{}"
# create an instance of CertificationMovieList200ResponseCertificationsARInner from a JSON string
certification_movie_list200_response_certifications_ar_inner_instance = CertificationMovieList200ResponseCertificationsARInner.from_json(json)
# print the JSON string representation of the object
print(CertificationMovieList200ResponseCertificationsARInner.to_json())

# convert the object into a dict
certification_movie_list200_response_certifications_ar_inner_dict = certification_movie_list200_response_certifications_ar_inner_instance.to_dict()
# create an instance of CertificationMovieList200ResponseCertificationsARInner from a dict
certification_movie_list200_response_certifications_ar_inner_from_dict = CertificationMovieList200ResponseCertificationsARInner.from_dict(certification_movie_list200_response_certifications_ar_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


