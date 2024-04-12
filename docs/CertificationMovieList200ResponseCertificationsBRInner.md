# CertificationMovieList200ResponseCertificationsBRInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certification** | **str** |  | [optional] 
**meaning** | **str** |  | [optional] 
**order** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.certification_movie_list200_response_certifications_br_inner import CertificationMovieList200ResponseCertificationsBRInner

# TODO update the JSON string below
json = "{}"
# create an instance of CertificationMovieList200ResponseCertificationsBRInner from a JSON string
certification_movie_list200_response_certifications_br_inner_instance = CertificationMovieList200ResponseCertificationsBRInner.from_json(json)
# print the JSON string representation of the object
print(CertificationMovieList200ResponseCertificationsBRInner.to_json())

# convert the object into a dict
certification_movie_list200_response_certifications_br_inner_dict = certification_movie_list200_response_certifications_br_inner_instance.to_dict()
# create an instance of CertificationMovieList200ResponseCertificationsBRInner from a dict
certification_movie_list200_response_certifications_br_inner_from_dict = CertificationMovieList200ResponseCertificationsBRInner.from_dict(certification_movie_list200_response_certifications_br_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


