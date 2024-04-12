# MovieUpcomingList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dates** | [**MovieUpcomingList200ResponseDates**](MovieUpcomingList200ResponseDates.md) |  | [optional] 
**page** | **int** |  | [optional] [default to 0]
**results** | [**List[MovieUpcomingList200ResponseResultsInner]**](MovieUpcomingList200ResponseResultsInner.md) |  | [optional] 
**total_pages** | **int** |  | [optional] [default to 0]
**total_results** | **int** |  | [optional] [default to 0]

## Example

```python
from tmdb_client.models.movie_upcoming_list200_response import MovieUpcomingList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MovieUpcomingList200Response from a JSON string
movie_upcoming_list200_response_instance = MovieUpcomingList200Response.from_json(json)
# print the JSON string representation of the object
print(MovieUpcomingList200Response.to_json())

# convert the object into a dict
movie_upcoming_list200_response_dict = movie_upcoming_list200_response_instance.to_dict()
# create an instance of MovieUpcomingList200Response from a dict
movie_upcoming_list200_response_from_dict = MovieUpcomingList200Response.from_dict(movie_upcoming_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


