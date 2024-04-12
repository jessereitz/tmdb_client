# MovieTranslations200ResponseTranslationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_3166_1** | **str** |  | [optional] 
**iso_639_1** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**english_name** | **str** |  | [optional] 
**data** | [**MovieTranslations200ResponseTranslationsInnerData**](MovieTranslations200ResponseTranslationsInnerData.md) |  | [optional] 

## Example

```python
from tmdb_client.models.movie_translations200_response_translations_inner import MovieTranslations200ResponseTranslationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MovieTranslations200ResponseTranslationsInner from a JSON string
movie_translations200_response_translations_inner_instance = MovieTranslations200ResponseTranslationsInner.from_json(json)
# print the JSON string representation of the object
print(MovieTranslations200ResponseTranslationsInner.to_json())

# convert the object into a dict
movie_translations200_response_translations_inner_dict = movie_translations200_response_translations_inner_instance.to_dict()
# create an instance of MovieTranslations200ResponseTranslationsInner from a dict
movie_translations200_response_translations_inner_from_dict = MovieTranslations200ResponseTranslationsInner.from_dict(movie_translations200_response_translations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


