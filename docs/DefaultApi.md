# openapi_client.DefaultApi

All URIs are relative to *https://api.themoviedb.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_add_favorite**](DefaultApi.md#account_add_favorite) | **POST** /3/account/{account_id}/favorite | Add Favorite
[**account_add_to_watchlist**](DefaultApi.md#account_add_to_watchlist) | **POST** /3/account/{account_id}/watchlist | Add To Watchlist
[**account_details**](DefaultApi.md#account_details) | **GET** /3/account/{account_id} | Details
[**account_favorite_tv**](DefaultApi.md#account_favorite_tv) | **GET** /3/account/{account_id}/favorite/tv | Favorite TV
[**account_get_favorites**](DefaultApi.md#account_get_favorites) | **GET** /3/account/{account_id}/favorite/movies | Favorite Movies
[**account_lists**](DefaultApi.md#account_lists) | **GET** /3/account/{account_id}/lists | Lists
[**account_rated_movies**](DefaultApi.md#account_rated_movies) | **GET** /3/account/{account_id}/rated/movies | Rated Movies
[**account_rated_tv**](DefaultApi.md#account_rated_tv) | **GET** /3/account/{account_id}/rated/tv | Rated TV
[**account_rated_tv_episodes**](DefaultApi.md#account_rated_tv_episodes) | **GET** /3/account/{account_id}/rated/tv/episodes | Rated TV Episodes
[**account_watchlist_movies**](DefaultApi.md#account_watchlist_movies) | **GET** /3/account/{account_id}/watchlist/movies | Watchlist Movies
[**account_watchlist_tv**](DefaultApi.md#account_watchlist_tv) | **GET** /3/account/{account_id}/watchlist/tv | Watchlist TV
[**alternative_names_copy**](DefaultApi.md#alternative_names_copy) | **GET** /3/network/{network_id}/images | Images
[**authentication_create_guest_session**](DefaultApi.md#authentication_create_guest_session) | **GET** /3/authentication/guest_session/new | Create Guest Session
[**authentication_create_request_token**](DefaultApi.md#authentication_create_request_token) | **GET** /3/authentication/token/new | Create Request Token
[**authentication_create_session**](DefaultApi.md#authentication_create_session) | **POST** /3/authentication/session/new | Create Session
[**authentication_create_session_from_login**](DefaultApi.md#authentication_create_session_from_login) | **POST** /3/authentication/token/validate_with_login | Create Session (with login)
[**authentication_create_session_from_v4_token**](DefaultApi.md#authentication_create_session_from_v4_token) | **POST** /3/authentication/session/convert/4 | Create Session (from v4 token)
[**authentication_delete_session**](DefaultApi.md#authentication_delete_session) | **DELETE** /3/authentication/session | Delete Session
[**authentication_validate_key**](DefaultApi.md#authentication_validate_key) | **GET** /3/authentication | Validate Key
[**certification_movie_list**](DefaultApi.md#certification_movie_list) | **GET** /3/certification/movie/list | Movie Certifications
[**certifications_tv_list**](DefaultApi.md#certifications_tv_list) | **GET** /3/certification/tv/list | TV Certifications
[**changes_movie_list**](DefaultApi.md#changes_movie_list) | **GET** /3/movie/changes | Movie List
[**changes_people_list**](DefaultApi.md#changes_people_list) | **GET** /3/person/changes | People List
[**changes_tv_list**](DefaultApi.md#changes_tv_list) | **GET** /3/tv/changes | TV List
[**collection_details**](DefaultApi.md#collection_details) | **GET** /3/collection/{collection_id} | Details
[**collection_images**](DefaultApi.md#collection_images) | **GET** /3/collection/{collection_id}/images | Images
[**collection_translations**](DefaultApi.md#collection_translations) | **GET** /3/collection/{collection_id}/translations | Translations
[**company_alternative_names**](DefaultApi.md#company_alternative_names) | **GET** /3/company/{company_id}/alternative_names | Alternative Names
[**company_details**](DefaultApi.md#company_details) | **GET** /3/company/{company_id} | Details
[**company_images**](DefaultApi.md#company_images) | **GET** /3/company/{company_id}/images | Images
[**configuration_countries**](DefaultApi.md#configuration_countries) | **GET** /3/configuration/countries | Countries
[**configuration_details**](DefaultApi.md#configuration_details) | **GET** /3/configuration | Details
[**configuration_jobs**](DefaultApi.md#configuration_jobs) | **GET** /3/configuration/jobs | Jobs
[**configuration_languages**](DefaultApi.md#configuration_languages) | **GET** /3/configuration/languages | Languages
[**configuration_primary_translations**](DefaultApi.md#configuration_primary_translations) | **GET** /3/configuration/primary_translations | Primary Translations
[**configuration_timezones**](DefaultApi.md#configuration_timezones) | **GET** /3/configuration/timezones | Timezones
[**credit_details**](DefaultApi.md#credit_details) | **GET** /3/credit/{credit_id} | Details
[**details_copy**](DefaultApi.md#details_copy) | **GET** /3/network/{network_id}/alternative_names | Alternative Names
[**discover_movie**](DefaultApi.md#discover_movie) | **GET** /3/discover/movie | Movie
[**discover_tv**](DefaultApi.md#discover_tv) | **GET** /3/discover/tv | TV
[**find_by_id**](DefaultApi.md#find_by_id) | **GET** /3/find/{external_id} | Find By ID
[**genre_movie_list**](DefaultApi.md#genre_movie_list) | **GET** /3/genre/movie/list | Movie List
[**genre_tv_list**](DefaultApi.md#genre_tv_list) | **GET** /3/genre/tv/list | TV List
[**guest_session_rated_movies**](DefaultApi.md#guest_session_rated_movies) | **GET** /3/guest_session/{guest_session_id}/rated/movies | Rated Movies
[**guest_session_rated_tv**](DefaultApi.md#guest_session_rated_tv) | **GET** /3/guest_session/{guest_session_id}/rated/tv | Rated TV
[**guest_session_rated_tv_episodes**](DefaultApi.md#guest_session_rated_tv_episodes) | **GET** /3/guest_session/{guest_session_id}/rated/tv/episodes | Rated TV Episodes
[**keyword_details**](DefaultApi.md#keyword_details) | **GET** /3/keyword/{keyword_id} | Details
[**keyword_movies**](DefaultApi.md#keyword_movies) | **GET** /3/keyword/{keyword_id}/movies | Movies
[**list_add_movie**](DefaultApi.md#list_add_movie) | **POST** /3/list/{list_id}/add_item | Add Movie
[**list_check_item_status**](DefaultApi.md#list_check_item_status) | **GET** /3/list/{list_id}/item_status | Check Item Status
[**list_clear**](DefaultApi.md#list_clear) | **POST** /3/list/{list_id}/clear | Clear
[**list_create**](DefaultApi.md#list_create) | **POST** /3/list | Create
[**list_delete**](DefaultApi.md#list_delete) | **DELETE** /3/list/{list_id} | Delete
[**list_details**](DefaultApi.md#list_details) | **GET** /3/list/{list_id} | Details
[**list_remove_movie**](DefaultApi.md#list_remove_movie) | **POST** /3/list/{list_id}/remove_item | Remove Movie
[**lists_copy**](DefaultApi.md#lists_copy) | **GET** /3/tv/{series_id}/lists | Lists
[**movie_account_states**](DefaultApi.md#movie_account_states) | **GET** /3/movie/{movie_id}/account_states | Account States
[**movie_add_rating**](DefaultApi.md#movie_add_rating) | **POST** /3/movie/{movie_id}/rating | Add Rating
[**movie_alternative_titles**](DefaultApi.md#movie_alternative_titles) | **GET** /3/movie/{movie_id}/alternative_titles | Alternative Titles
[**movie_changes**](DefaultApi.md#movie_changes) | **GET** /3/movie/{movie_id}/changes | Changes
[**movie_credits**](DefaultApi.md#movie_credits) | **GET** /3/movie/{movie_id}/credits | Credits
[**movie_delete_rating**](DefaultApi.md#movie_delete_rating) | **DELETE** /3/movie/{movie_id}/rating | Delete Rating
[**movie_details**](DefaultApi.md#movie_details) | **GET** /3/movie/{movie_id} | Details
[**movie_external_ids**](DefaultApi.md#movie_external_ids) | **GET** /3/movie/{movie_id}/external_ids | External IDs
[**movie_images**](DefaultApi.md#movie_images) | **GET** /3/movie/{movie_id}/images | Images
[**movie_keywords**](DefaultApi.md#movie_keywords) | **GET** /3/movie/{movie_id}/keywords | Keywords
[**movie_latest_id**](DefaultApi.md#movie_latest_id) | **GET** /3/movie/latest | Latest
[**movie_lists**](DefaultApi.md#movie_lists) | **GET** /3/movie/{movie_id}/lists | Lists
[**movie_now_playing_list**](DefaultApi.md#movie_now_playing_list) | **GET** /3/movie/now_playing | Now Playing
[**movie_popular_list**](DefaultApi.md#movie_popular_list) | **GET** /3/movie/popular | Popular
[**movie_recommendations**](DefaultApi.md#movie_recommendations) | **GET** /3/movie/{movie_id}/recommendations | Recommendations
[**movie_release_dates**](DefaultApi.md#movie_release_dates) | **GET** /3/movie/{movie_id}/release_dates | Release Dates
[**movie_reviews**](DefaultApi.md#movie_reviews) | **GET** /3/movie/{movie_id}/reviews | Reviews
[**movie_similar**](DefaultApi.md#movie_similar) | **GET** /3/movie/{movie_id}/similar | Similar
[**movie_top_rated_list**](DefaultApi.md#movie_top_rated_list) | **GET** /3/movie/top_rated | Top Rated
[**movie_translations**](DefaultApi.md#movie_translations) | **GET** /3/movie/{movie_id}/translations | Translations
[**movie_upcoming_list**](DefaultApi.md#movie_upcoming_list) | **GET** /3/movie/upcoming | Upcoming
[**movie_videos**](DefaultApi.md#movie_videos) | **GET** /3/movie/{movie_id}/videos | Videos
[**movie_watch_providers**](DefaultApi.md#movie_watch_providers) | **GET** /3/movie/{movie_id}/watch/providers | Watch Providers
[**network_details**](DefaultApi.md#network_details) | **GET** /3/network/{network_id} | Details
[**person_changes**](DefaultApi.md#person_changes) | **GET** /3/person/{person_id}/changes | Changes
[**person_combined_credits**](DefaultApi.md#person_combined_credits) | **GET** /3/person/{person_id}/combined_credits | Combined Credits
[**person_details**](DefaultApi.md#person_details) | **GET** /3/person/{person_id} | Details
[**person_external_ids**](DefaultApi.md#person_external_ids) | **GET** /3/person/{person_id}/external_ids | External IDs
[**person_images**](DefaultApi.md#person_images) | **GET** /3/person/{person_id}/images | Images
[**person_latest_id**](DefaultApi.md#person_latest_id) | **GET** /3/person/latest | Latest
[**person_movie_credits**](DefaultApi.md#person_movie_credits) | **GET** /3/person/{person_id}/movie_credits | Movie Credits
[**person_popular_list**](DefaultApi.md#person_popular_list) | **GET** /3/person/popular | Popular
[**person_tagged_images**](DefaultApi.md#person_tagged_images) | **GET** /3/person/{person_id}/tagged_images | Tagged Images
[**person_tv_credits**](DefaultApi.md#person_tv_credits) | **GET** /3/person/{person_id}/tv_credits | TV Credits
[**review_details**](DefaultApi.md#review_details) | **GET** /3/review/{review_id} | Details
[**search_collection**](DefaultApi.md#search_collection) | **GET** /3/search/collection | Collection
[**search_company**](DefaultApi.md#search_company) | **GET** /3/search/company | Company
[**search_keyword**](DefaultApi.md#search_keyword) | **GET** /3/search/keyword | Keyword
[**search_movie**](DefaultApi.md#search_movie) | **GET** /3/search/movie | Movie
[**search_multi**](DefaultApi.md#search_multi) | **GET** /3/search/multi | Multi
[**search_person**](DefaultApi.md#search_person) | **GET** /3/search/person | Person
[**search_tv**](DefaultApi.md#search_tv) | **GET** /3/search/tv | TV
[**translations**](DefaultApi.md#translations) | **GET** /3/person/{person_id}/translations | Translations
[**trending_all**](DefaultApi.md#trending_all) | **GET** /3/trending/all/{time_window} | All
[**trending_movies**](DefaultApi.md#trending_movies) | **GET** /3/trending/movie/{time_window} | Movies
[**trending_people**](DefaultApi.md#trending_people) | **GET** /3/trending/person/{time_window} | People
[**trending_tv**](DefaultApi.md#trending_tv) | **GET** /3/trending/tv/{time_window} | TV
[**tv_episode_account_states**](DefaultApi.md#tv_episode_account_states) | **GET** /3/tv/{series_id}/season/{season_number}/episode/{episode_number}/account_states | Account States
[**tv_episode_add_rating**](DefaultApi.md#tv_episode_add_rating) | **POST** /3/tv/{series_id}/season/{season_number}/episode/{episode_number}/rating | Add Rating
[**tv_episode_changes_by_id**](DefaultApi.md#tv_episode_changes_by_id) | **GET** /3/tv/episode/{episode_id}/changes | Changes
[**tv_episode_credits**](DefaultApi.md#tv_episode_credits) | **GET** /3/tv/{series_id}/season/{season_number}/episode/{episode_number}/credits | Credits
[**tv_episode_delete_rating**](DefaultApi.md#tv_episode_delete_rating) | **DELETE** /3/tv/{series_id}/season/{season_number}/episode/{episode_number}/rating | Delete Rating
[**tv_episode_details**](DefaultApi.md#tv_episode_details) | **GET** /3/tv/{series_id}/season/{season_number}/episode/{episode_number} | Details
[**tv_episode_external_ids**](DefaultApi.md#tv_episode_external_ids) | **GET** /3/tv/{series_id}/season/{season_number}/episode/{episode_number}/external_ids | External IDs
[**tv_episode_group_details**](DefaultApi.md#tv_episode_group_details) | **GET** /3/tv/episode_group/{tv_episode_group_id} | Details
[**tv_episode_images**](DefaultApi.md#tv_episode_images) | **GET** /3/tv/{series_id}/season/{season_number}/episode/{episode_number}/images | Images
[**tv_episode_translations**](DefaultApi.md#tv_episode_translations) | **GET** /3/tv/{series_id}/season/{season_number}/episode/{episode_number}/translations | Translations
[**tv_episode_videos**](DefaultApi.md#tv_episode_videos) | **GET** /3/tv/{series_id}/season/{season_number}/episode/{episode_number}/videos | Videos
[**tv_season_account_states**](DefaultApi.md#tv_season_account_states) | **GET** /3/tv/{series_id}/season/{season_number}/account_states | Account States
[**tv_season_aggregate_credits**](DefaultApi.md#tv_season_aggregate_credits) | **GET** /3/tv/{series_id}/season/{season_number}/aggregate_credits | Aggregate Credits
[**tv_season_changes_by_id**](DefaultApi.md#tv_season_changes_by_id) | **GET** /3/tv/season/{season_id}/changes | Changes
[**tv_season_credits**](DefaultApi.md#tv_season_credits) | **GET** /3/tv/{series_id}/season/{season_number}/credits | Credits
[**tv_season_details**](DefaultApi.md#tv_season_details) | **GET** /3/tv/{series_id}/season/{season_number} | Details
[**tv_season_external_ids**](DefaultApi.md#tv_season_external_ids) | **GET** /3/tv/{series_id}/season/{season_number}/external_ids | External IDs
[**tv_season_images**](DefaultApi.md#tv_season_images) | **GET** /3/tv/{series_id}/season/{season_number}/images | Images
[**tv_season_translations**](DefaultApi.md#tv_season_translations) | **GET** /3/tv/{series_id}/season/{season_number}/translations | Translations
[**tv_season_videos**](DefaultApi.md#tv_season_videos) | **GET** /3/tv/{series_id}/season/{season_number}/videos | Videos
[**tv_season_watch_providers**](DefaultApi.md#tv_season_watch_providers) | **GET** /3/tv/{series_id}/season/{season_number}/watch/providers | Watch Providers
[**tv_series_account_states**](DefaultApi.md#tv_series_account_states) | **GET** /3/tv/{series_id}/account_states | Account States
[**tv_series_add_rating**](DefaultApi.md#tv_series_add_rating) | **POST** /3/tv/{series_id}/rating | Add Rating
[**tv_series_aggregate_credits**](DefaultApi.md#tv_series_aggregate_credits) | **GET** /3/tv/{series_id}/aggregate_credits | Aggregate Credits
[**tv_series_airing_today_list**](DefaultApi.md#tv_series_airing_today_list) | **GET** /3/tv/airing_today | Airing Today
[**tv_series_alternative_titles**](DefaultApi.md#tv_series_alternative_titles) | **GET** /3/tv/{series_id}/alternative_titles | Alternative Titles
[**tv_series_changes**](DefaultApi.md#tv_series_changes) | **GET** /3/tv/{series_id}/changes | Changes
[**tv_series_content_ratings**](DefaultApi.md#tv_series_content_ratings) | **GET** /3/tv/{series_id}/content_ratings | Content Ratings
[**tv_series_credits**](DefaultApi.md#tv_series_credits) | **GET** /3/tv/{series_id}/credits | Credits
[**tv_series_delete_rating**](DefaultApi.md#tv_series_delete_rating) | **DELETE** /3/tv/{series_id}/rating | Delete Rating
[**tv_series_details**](DefaultApi.md#tv_series_details) | **GET** /3/tv/{series_id} | Details
[**tv_series_episode_groups**](DefaultApi.md#tv_series_episode_groups) | **GET** /3/tv/{series_id}/episode_groups | Episode Groups
[**tv_series_external_ids**](DefaultApi.md#tv_series_external_ids) | **GET** /3/tv/{series_id}/external_ids | External IDs
[**tv_series_images**](DefaultApi.md#tv_series_images) | **GET** /3/tv/{series_id}/images | Images
[**tv_series_keywords**](DefaultApi.md#tv_series_keywords) | **GET** /3/tv/{series_id}/keywords | Keywords
[**tv_series_latest_id**](DefaultApi.md#tv_series_latest_id) | **GET** /3/tv/latest | Latest
[**tv_series_on_the_air_list**](DefaultApi.md#tv_series_on_the_air_list) | **GET** /3/tv/on_the_air | On The Air
[**tv_series_popular_list**](DefaultApi.md#tv_series_popular_list) | **GET** /3/tv/popular | Popular
[**tv_series_recommendations**](DefaultApi.md#tv_series_recommendations) | **GET** /3/tv/{series_id}/recommendations | Recommendations
[**tv_series_reviews**](DefaultApi.md#tv_series_reviews) | **GET** /3/tv/{series_id}/reviews | Reviews
[**tv_series_screened_theatrically**](DefaultApi.md#tv_series_screened_theatrically) | **GET** /3/tv/{series_id}/screened_theatrically | Screened Theatrically
[**tv_series_similar**](DefaultApi.md#tv_series_similar) | **GET** /3/tv/{series_id}/similar | Similar
[**tv_series_top_rated_list**](DefaultApi.md#tv_series_top_rated_list) | **GET** /3/tv/top_rated | Top Rated
[**tv_series_translations**](DefaultApi.md#tv_series_translations) | **GET** /3/tv/{series_id}/translations | Translations
[**tv_series_videos**](DefaultApi.md#tv_series_videos) | **GET** /3/tv/{series_id}/videos | Videos
[**tv_series_watch_providers**](DefaultApi.md#tv_series_watch_providers) | **GET** /3/tv/{series_id}/watch/providers | Watch Providers
[**watch_provider_tv_list**](DefaultApi.md#watch_provider_tv_list) | **GET** /3/watch/providers/tv | TV Providers
[**watch_providers_available_regions**](DefaultApi.md#watch_providers_available_regions) | **GET** /3/watch/providers/regions | Available Regions
[**watch_providers_movie_list**](DefaultApi.md#watch_providers_movie_list) | **GET** /3/watch/providers/movie | Movie Providers


# **account_add_favorite**
> MovieAddRating200Response account_add_favorite(account_id, session_id=session_id, movie_add_rating_request=movie_add_rating_request)

Add Favorite



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_add_rating200_response import MovieAddRating200Response
from openapi_client.models.movie_add_rating_request import MovieAddRatingRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    account_id = 56 # int | 
    session_id = 'session_id_example' # str |  (optional)
    movie_add_rating_request = {"media_type":"movie","media_id":550,"favorite":true} # MovieAddRatingRequest |  (optional)

    try:
        # Add Favorite
        api_response = api_instance.account_add_favorite(account_id, session_id=session_id, movie_add_rating_request=movie_add_rating_request)
        print("The response of DefaultApi->account_add_favorite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->account_add_favorite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **session_id** | **str**|  | [optional] 
 **movie_add_rating_request** | [**MovieAddRatingRequest**](MovieAddRatingRequest.md)|  | [optional] 

### Return type

[**MovieAddRating200Response**](MovieAddRating200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_add_to_watchlist**
> MovieAddRating200Response account_add_to_watchlist(account_id, session_id=session_id, movie_add_rating_request=movie_add_rating_request)

Add To Watchlist



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_add_rating200_response import MovieAddRating200Response
from openapi_client.models.movie_add_rating_request import MovieAddRatingRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    account_id = 56 # int | 
    session_id = 'session_id_example' # str |  (optional)
    movie_add_rating_request = {"media_type":"movie","media_id":11,"watchlist":true} # MovieAddRatingRequest |  (optional)

    try:
        # Add To Watchlist
        api_response = api_instance.account_add_to_watchlist(account_id, session_id=session_id, movie_add_rating_request=movie_add_rating_request)
        print("The response of DefaultApi->account_add_to_watchlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->account_add_to_watchlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **session_id** | **str**|  | [optional] 
 **movie_add_rating_request** | [**MovieAddRatingRequest**](MovieAddRatingRequest.md)|  | [optional] 

### Return type

[**MovieAddRating200Response**](MovieAddRating200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_details**
> AccountDetails200Response account_details(account_id, session_id=session_id)

Details



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.account_details200_response import AccountDetails200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    account_id = null # int |  (default to null)
    session_id = 'session_id_example' # str |  (optional)

    try:
        # Details
        api_response = api_instance.account_details(account_id, session_id=session_id)
        print("The response of DefaultApi->account_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->account_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | [default to null]
 **session_id** | **str**|  | [optional] 

### Return type

[**AccountDetails200Response**](AccountDetails200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_favorite_tv**
> AccountFavoriteTv200Response account_favorite_tv(account_id, language=language, page=page, session_id=session_id, sort_by=sort_by)

Favorite TV



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.account_favorite_tv200_response import AccountFavoriteTv200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    account_id = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)
    session_id = 'session_id_example' # str |  (optional)
    sort_by = 'created_at.asc' # str |  (optional) (default to 'created_at.asc')

    try:
        # Favorite TV
        api_response = api_instance.account_favorite_tv(account_id, language=language, page=page, session_id=session_id, sort_by=sort_by)
        print("The response of DefaultApi->account_favorite_tv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->account_favorite_tv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]
 **session_id** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] [default to &#39;created_at.asc&#39;]

### Return type

[**AccountFavoriteTv200Response**](AccountFavoriteTv200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_get_favorites**
> AccountGetFavorites200Response account_get_favorites(account_id, language=language, page=page, session_id=session_id, sort_by=sort_by)

Favorite Movies



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.account_get_favorites200_response import AccountGetFavorites200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    account_id = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)
    session_id = 'session_id_example' # str |  (optional)
    sort_by = 'created_at.asc' # str |  (optional) (default to 'created_at.asc')

    try:
        # Favorite Movies
        api_response = api_instance.account_get_favorites(account_id, language=language, page=page, session_id=session_id, sort_by=sort_by)
        print("The response of DefaultApi->account_get_favorites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->account_get_favorites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]
 **session_id** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] [default to &#39;created_at.asc&#39;]

### Return type

[**AccountGetFavorites200Response**](AccountGetFavorites200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_lists**
> AccountLists200Response account_lists(account_id, page=page, session_id=session_id)

Lists



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.account_lists200_response import AccountLists200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    account_id = 56 # int | 
    page = 1 # int |  (optional) (default to 1)
    session_id = 'session_id_example' # str |  (optional)

    try:
        # Lists
        api_response = api_instance.account_lists(account_id, page=page, session_id=session_id)
        print("The response of DefaultApi->account_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->account_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **session_id** | **str**|  | [optional] 

### Return type

[**AccountLists200Response**](AccountLists200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_rated_movies**
> AccountRatedMovies200Response account_rated_movies(account_id, language=language, page=page, session_id=session_id, sort_by=sort_by)

Rated Movies



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.account_rated_movies200_response import AccountRatedMovies200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    account_id = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)
    session_id = 'session_id_example' # str |  (optional)
    sort_by = 'created_at.asc' # str |  (optional) (default to 'created_at.asc')

    try:
        # Rated Movies
        api_response = api_instance.account_rated_movies(account_id, language=language, page=page, session_id=session_id, sort_by=sort_by)
        print("The response of DefaultApi->account_rated_movies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->account_rated_movies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]
 **session_id** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] [default to &#39;created_at.asc&#39;]

### Return type

[**AccountRatedMovies200Response**](AccountRatedMovies200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_rated_tv**
> AccountRatedTv200Response account_rated_tv(account_id, language=language, page=page, session_id=session_id, sort_by=sort_by)

Rated TV



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.account_rated_tv200_response import AccountRatedTv200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    account_id = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)
    session_id = 'session_id_example' # str |  (optional)
    sort_by = 'created_at.asc' # str |  (optional) (default to 'created_at.asc')

    try:
        # Rated TV
        api_response = api_instance.account_rated_tv(account_id, language=language, page=page, session_id=session_id, sort_by=sort_by)
        print("The response of DefaultApi->account_rated_tv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->account_rated_tv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]
 **session_id** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] [default to &#39;created_at.asc&#39;]

### Return type

[**AccountRatedTv200Response**](AccountRatedTv200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_rated_tv_episodes**
> AccountRatedTvEpisodes200Response account_rated_tv_episodes(account_id, language=language, page=page, session_id=session_id, sort_by=sort_by)

Rated TV Episodes



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.account_rated_tv_episodes200_response import AccountRatedTvEpisodes200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    account_id = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)
    session_id = 'session_id_example' # str |  (optional)
    sort_by = 'created_at.asc' # str |  (optional) (default to 'created_at.asc')

    try:
        # Rated TV Episodes
        api_response = api_instance.account_rated_tv_episodes(account_id, language=language, page=page, session_id=session_id, sort_by=sort_by)
        print("The response of DefaultApi->account_rated_tv_episodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->account_rated_tv_episodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]
 **session_id** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] [default to &#39;created_at.asc&#39;]

### Return type

[**AccountRatedTvEpisodes200Response**](AccountRatedTvEpisodes200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_watchlist_movies**
> AccountWatchlistMovies200Response account_watchlist_movies(account_id, language=language, page=page, session_id=session_id, sort_by=sort_by)

Watchlist Movies



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.account_watchlist_movies200_response import AccountWatchlistMovies200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    account_id = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)
    session_id = 'session_id_example' # str |  (optional)
    sort_by = 'created_at.asc' # str |  (optional) (default to 'created_at.asc')

    try:
        # Watchlist Movies
        api_response = api_instance.account_watchlist_movies(account_id, language=language, page=page, session_id=session_id, sort_by=sort_by)
        print("The response of DefaultApi->account_watchlist_movies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->account_watchlist_movies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]
 **session_id** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] [default to &#39;created_at.asc&#39;]

### Return type

[**AccountWatchlistMovies200Response**](AccountWatchlistMovies200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_watchlist_tv**
> AccountWatchlistTv200Response account_watchlist_tv(account_id, language=language, page=page, session_id=session_id, sort_by=sort_by)

Watchlist TV



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.account_watchlist_tv200_response import AccountWatchlistTv200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    account_id = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)
    session_id = 'session_id_example' # str |  (optional)
    sort_by = 'created_at.asc' # str |  (optional) (default to 'created_at.asc')

    try:
        # Watchlist TV
        api_response = api_instance.account_watchlist_tv(account_id, language=language, page=page, session_id=session_id, sort_by=sort_by)
        print("The response of DefaultApi->account_watchlist_tv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->account_watchlist_tv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]
 **session_id** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] [default to &#39;created_at.asc&#39;]

### Return type

[**AccountWatchlistTv200Response**](AccountWatchlistTv200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alternative_names_copy**
> AlternativeNamesCopy200Response alternative_names_copy(network_id)

Images

Get the TV network logos by id.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.alternative_names_copy200_response import AlternativeNamesCopy200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    network_id = 56 # int | 

    try:
        # Images
        api_response = api_instance.alternative_names_copy(network_id)
        print("The response of DefaultApi->alternative_names_copy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->alternative_names_copy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **int**|  | 

### Return type

[**AlternativeNamesCopy200Response**](AlternativeNamesCopy200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_create_guest_session**
> AuthenticationCreateGuestSession200Response authentication_create_guest_session()

Create Guest Session



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.authentication_create_guest_session200_response import AuthenticationCreateGuestSession200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Create Guest Session
        api_response = api_instance.authentication_create_guest_session()
        print("The response of DefaultApi->authentication_create_guest_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->authentication_create_guest_session: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthenticationCreateGuestSession200Response**](AuthenticationCreateGuestSession200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_create_request_token**
> AuthenticationCreateRequestToken200Response authentication_create_request_token()

Create Request Token



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.authentication_create_request_token200_response import AuthenticationCreateRequestToken200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Create Request Token
        api_response = api_instance.authentication_create_request_token()
        print("The response of DefaultApi->authentication_create_request_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->authentication_create_request_token: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthenticationCreateRequestToken200Response**](AuthenticationCreateRequestToken200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_create_session**
> AuthenticationCreateSession200Response authentication_create_session(movie_add_rating_request=movie_add_rating_request)

Create Session



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.authentication_create_session200_response import AuthenticationCreateSession200Response
from openapi_client.models.movie_add_rating_request import MovieAddRatingRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    movie_add_rating_request = {"request_token":"6bc047b88f669d1fb86574f06381005d93d3517a"} # MovieAddRatingRequest |  (optional)

    try:
        # Create Session
        api_response = api_instance.authentication_create_session(movie_add_rating_request=movie_add_rating_request)
        print("The response of DefaultApi->authentication_create_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->authentication_create_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_add_rating_request** | [**MovieAddRatingRequest**](MovieAddRatingRequest.md)|  | [optional] 

### Return type

[**AuthenticationCreateSession200Response**](AuthenticationCreateSession200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_create_session_from_login**
> AuthenticationCreateSessionFromLogin200Response authentication_create_session_from_login(movie_add_rating_request=movie_add_rating_request)

Create Session (with login)

This method allows an application to validate a request token by entering a username and password.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.authentication_create_session_from_login200_response import AuthenticationCreateSessionFromLogin200Response
from openapi_client.models.movie_add_rating_request import MovieAddRatingRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    movie_add_rating_request = {"username":"johnny_appleseed","password":"test123","request_token":"1531f1a558c8357ce8990cf887ff196e8f5402ec"} # MovieAddRatingRequest |  (optional)

    try:
        # Create Session (with login)
        api_response = api_instance.authentication_create_session_from_login(movie_add_rating_request=movie_add_rating_request)
        print("The response of DefaultApi->authentication_create_session_from_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->authentication_create_session_from_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_add_rating_request** | [**MovieAddRatingRequest**](MovieAddRatingRequest.md)|  | [optional] 

### Return type

[**AuthenticationCreateSessionFromLogin200Response**](AuthenticationCreateSessionFromLogin200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_create_session_from_v4_token**
> AuthenticationCreateSessionFromV4Token200Response authentication_create_session_from_v4_token(movie_add_rating_request=movie_add_rating_request)

Create Session (from v4 token)



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.authentication_create_session_from_v4_token200_response import AuthenticationCreateSessionFromV4Token200Response
from openapi_client.models.movie_add_rating_request import MovieAddRatingRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    movie_add_rating_request = {"access_token":"eyK0eXAiOiJAV1QiLCJhbGciOiUIUzI1NiJ9.eyJhdWQiOiI0Ozc2YzA1ZTg4YTY1Yzk0MjFjZDI1NmBiYzRiNGE0NyIsInN1YiI6IjRiYzg4OTJhMDE3YTNjMGY5MjAwMDAwMiIsInNjb3BlayI6WyJhcGlfcmVhZCJdLCL2ZXJzaW9uIjoxfQ.Bn660W0Vi-_AI5HvwIEqtc2s5mAXDknBnTrUREZYH7A"} # MovieAddRatingRequest |  (optional)

    try:
        # Create Session (from v4 token)
        api_response = api_instance.authentication_create_session_from_v4_token(movie_add_rating_request=movie_add_rating_request)
        print("The response of DefaultApi->authentication_create_session_from_v4_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->authentication_create_session_from_v4_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_add_rating_request** | [**MovieAddRatingRequest**](MovieAddRatingRequest.md)|  | [optional] 

### Return type

[**AuthenticationCreateSessionFromV4Token200Response**](AuthenticationCreateSessionFromV4Token200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_delete_session**
> AuthenticationDeleteSession200Response authentication_delete_session(movie_add_rating_request=movie_add_rating_request)

Delete Session



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.authentication_delete_session200_response import AuthenticationDeleteSession200Response
from openapi_client.models.movie_add_rating_request import MovieAddRatingRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    movie_add_rating_request = {"session_id":"2629f70fb498edc263a0adb99118ac41f0053e8c"} # MovieAddRatingRequest |  (optional)

    try:
        # Delete Session
        api_response = api_instance.authentication_delete_session(movie_add_rating_request=movie_add_rating_request)
        print("The response of DefaultApi->authentication_delete_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->authentication_delete_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_add_rating_request** | [**MovieAddRatingRequest**](MovieAddRatingRequest.md)|  | [optional] 

### Return type

[**AuthenticationDeleteSession200Response**](AuthenticationDeleteSession200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_validate_key**
> AuthenticationValidateKey200Response authentication_validate_key()

Validate Key

Test your API Key to see if it's valid.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.authentication_validate_key200_response import AuthenticationValidateKey200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Validate Key
        api_response = api_instance.authentication_validate_key()
        print("The response of DefaultApi->authentication_validate_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->authentication_validate_key: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthenticationValidateKey200Response**](AuthenticationValidateKey200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |
**401** | 401 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **certification_movie_list**
> CertificationMovieList200Response certification_movie_list()

Movie Certifications

Get an up to date list of the officially supported movie certifications on TMDB.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.certification_movie_list200_response import CertificationMovieList200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Movie Certifications
        api_response = api_instance.certification_movie_list()
        print("The response of DefaultApi->certification_movie_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->certification_movie_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CertificationMovieList200Response**](CertificationMovieList200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **certifications_tv_list**
> CertificationsTvList200Response certifications_tv_list()

TV Certifications



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.certifications_tv_list200_response import CertificationsTvList200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # TV Certifications
        api_response = api_instance.certifications_tv_list()
        print("The response of DefaultApi->certifications_tv_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->certifications_tv_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CertificationsTvList200Response**](CertificationsTvList200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **changes_movie_list**
> ChangesMovieList200Response changes_movie_list(end_date=end_date, page=page, start_date=start_date)

Movie List

Get a list of all of the movie ids that have been changed in the past 24 hours.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.changes_movie_list200_response import ChangesMovieList200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    end_date = '2013-10-20' # date |  (optional)
    page = 1 # int |  (optional) (default to 1)
    start_date = '2013-10-20' # date |  (optional)

    try:
        # Movie List
        api_response = api_instance.changes_movie_list(end_date=end_date, page=page, start_date=start_date)
        print("The response of DefaultApi->changes_movie_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->changes_movie_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **date**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **start_date** | **date**|  | [optional] 

### Return type

[**ChangesMovieList200Response**](ChangesMovieList200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **changes_people_list**
> ChangesPeopleList200Response changes_people_list(end_date=end_date, page=page, start_date=start_date)

People List



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.changes_people_list200_response import ChangesPeopleList200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    end_date = '2013-10-20' # date |  (optional)
    page = 1 # int |  (optional) (default to 1)
    start_date = '2013-10-20' # date |  (optional)

    try:
        # People List
        api_response = api_instance.changes_people_list(end_date=end_date, page=page, start_date=start_date)
        print("The response of DefaultApi->changes_people_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->changes_people_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **date**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **start_date** | **date**|  | [optional] 

### Return type

[**ChangesPeopleList200Response**](ChangesPeopleList200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **changes_tv_list**
> ChangesTvList200Response changes_tv_list(end_date=end_date, page=page, start_date=start_date)

TV List



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.changes_tv_list200_response import ChangesTvList200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    end_date = '2013-10-20' # date |  (optional)
    page = 1 # int |  (optional) (default to 1)
    start_date = '2013-10-20' # date |  (optional)

    try:
        # TV List
        api_response = api_instance.changes_tv_list(end_date=end_date, page=page, start_date=start_date)
        print("The response of DefaultApi->changes_tv_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->changes_tv_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **date**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **start_date** | **date**|  | [optional] 

### Return type

[**ChangesTvList200Response**](ChangesTvList200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collection_details**
> CollectionDetails200Response collection_details(collection_id, language=language)

Details

Get collection details by ID.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.collection_details200_response import CollectionDetails200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    collection_id = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Details
        api_response = api_instance.collection_details(collection_id, language=language)
        print("The response of DefaultApi->collection_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->collection_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**CollectionDetails200Response**](CollectionDetails200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collection_images**
> CollectionImages200Response collection_images(collection_id, include_image_language=include_image_language, language=language)

Images

Get the images that belong to a collection.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.collection_images200_response import CollectionImages200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    collection_id = 56 # int | 
    include_image_language = 'include_image_language_example' # str | specify a comma separated list of ISO-639-1 values to query, for example: `en,null` (optional)
    language = 'language_example' # str |  (optional)

    try:
        # Images
        api_response = api_instance.collection_images(collection_id, include_image_language=include_image_language, language=language)
        print("The response of DefaultApi->collection_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->collection_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**|  | 
 **include_image_language** | **str**| specify a comma separated list of ISO-639-1 values to query, for example: &#x60;en,null&#x60; | [optional] 
 **language** | **str**|  | [optional] 

### Return type

[**CollectionImages200Response**](CollectionImages200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collection_translations**
> CollectionTranslations200Response collection_translations(collection_id)

Translations



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.collection_translations200_response import CollectionTranslations200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    collection_id = 56 # int | 

    try:
        # Translations
        api_response = api_instance.collection_translations(collection_id)
        print("The response of DefaultApi->collection_translations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->collection_translations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**|  | 

### Return type

[**CollectionTranslations200Response**](CollectionTranslations200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_alternative_names**
> CompanyAlternativeNames200Response company_alternative_names(company_id)

Alternative Names

Get the company details by ID.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.company_alternative_names200_response import CompanyAlternativeNames200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    company_id = 56 # int | 

    try:
        # Alternative Names
        api_response = api_instance.company_alternative_names(company_id)
        print("The response of DefaultApi->company_alternative_names:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->company_alternative_names: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**|  | 

### Return type

[**CompanyAlternativeNames200Response**](CompanyAlternativeNames200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_details**
> CompanyDetails200Response company_details(company_id)

Details

Get the company details by ID.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.company_details200_response import CompanyDetails200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    company_id = 56 # int | 

    try:
        # Details
        api_response = api_instance.company_details(company_id)
        print("The response of DefaultApi->company_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->company_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**|  | 

### Return type

[**CompanyDetails200Response**](CompanyDetails200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_images**
> CompanyImages200Response company_images(company_id)

Images

Get the company logos by id.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.company_images200_response import CompanyImages200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    company_id = 56 # int | 

    try:
        # Images
        api_response = api_instance.company_images(company_id)
        print("The response of DefaultApi->company_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->company_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**|  | 

### Return type

[**CompanyImages200Response**](CompanyImages200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_countries**
> List[WatchProvidersAvailableRegions200ResponseResultsInner] configuration_countries(language=language)

Countries

Get the list of countries (ISO 3166-1 tags) used throughout TMDB.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.watch_providers_available_regions200_response_results_inner import WatchProvidersAvailableRegions200ResponseResultsInner
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Countries
        api_response = api_instance.configuration_countries(language=language)
        print("The response of DefaultApi->configuration_countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->configuration_countries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**List[WatchProvidersAvailableRegions200ResponseResultsInner]**](WatchProvidersAvailableRegions200ResponseResultsInner.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_details**
> ConfigurationDetails200Response configuration_details()

Details

Query the API configuration details.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.configuration_details200_response import ConfigurationDetails200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Details
        api_response = api_instance.configuration_details()
        print("The response of DefaultApi->configuration_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->configuration_details: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ConfigurationDetails200Response**](ConfigurationDetails200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_jobs**
> List[ConfigurationJobs200ResponseInner] configuration_jobs()

Jobs

Get the list of the jobs and departments we use on TMDB.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.configuration_jobs200_response_inner import ConfigurationJobs200ResponseInner
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Jobs
        api_response = api_instance.configuration_jobs()
        print("The response of DefaultApi->configuration_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->configuration_jobs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ConfigurationJobs200ResponseInner]**](ConfigurationJobs200ResponseInner.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_languages**
> List[ConfigurationLanguages200ResponseInner] configuration_languages()

Languages

Get the list of languages (ISO 639-1 tags) used throughout TMDB.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.configuration_languages200_response_inner import ConfigurationLanguages200ResponseInner
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Languages
        api_response = api_instance.configuration_languages()
        print("The response of DefaultApi->configuration_languages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->configuration_languages: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ConfigurationLanguages200ResponseInner]**](ConfigurationLanguages200ResponseInner.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_primary_translations**
> List[str] configuration_primary_translations()

Primary Translations

Get a list of the officially supported translations on TMDB.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Primary Translations
        api_response = api_instance.configuration_primary_translations()
        print("The response of DefaultApi->configuration_primary_translations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->configuration_primary_translations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_timezones**
> List[ConfigurationTimezones200ResponseInner] configuration_timezones()

Timezones

Get the list of timezones used throughout TMDB.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.configuration_timezones200_response_inner import ConfigurationTimezones200ResponseInner
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Timezones
        api_response = api_instance.configuration_timezones()
        print("The response of DefaultApi->configuration_timezones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->configuration_timezones: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ConfigurationTimezones200ResponseInner]**](ConfigurationTimezones200ResponseInner.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_details**
> CreditDetails200Response credit_details(credit_id)

Details

Get a movie or TV credit details by ID.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.credit_details200_response import CreditDetails200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    credit_id = 'credit_id_example' # str | 

    try:
        # Details
        api_response = api_instance.credit_details(credit_id)
        print("The response of DefaultApi->credit_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->credit_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_id** | **str**|  | 

### Return type

[**CreditDetails200Response**](CreditDetails200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **details_copy**
> DetailsCopy200Response details_copy(network_id)

Alternative Names

Get the alternative names of a network.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.details_copy200_response import DetailsCopy200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    network_id = 56 # int | 

    try:
        # Alternative Names
        api_response = api_instance.details_copy(network_id)
        print("The response of DefaultApi->details_copy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->details_copy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **int**|  | 

### Return type

[**DetailsCopy200Response**](DetailsCopy200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_movie**
> DiscoverMovie200Response discover_movie(certification=certification, certification_gte=certification_gte, certification_lte=certification_lte, certification_country=certification_country, include_adult=include_adult, include_video=include_video, language=language, page=page, primary_release_year=primary_release_year, primary_release_date_gte=primary_release_date_gte, primary_release_date_lte=primary_release_date_lte, region=region, release_date_gte=release_date_gte, release_date_lte=release_date_lte, sort_by=sort_by, vote_average_gte=vote_average_gte, vote_average_lte=vote_average_lte, vote_count_gte=vote_count_gte, vote_count_lte=vote_count_lte, watch_region=watch_region, with_cast=with_cast, with_companies=with_companies, with_crew=with_crew, with_genres=with_genres, with_keywords=with_keywords, with_origin_country=with_origin_country, with_original_language=with_original_language, with_people=with_people, with_release_type=with_release_type, with_runtime_gte=with_runtime_gte, with_runtime_lte=with_runtime_lte, with_watch_monetization_types=with_watch_monetization_types, with_watch_providers=with_watch_providers, without_companies=without_companies, without_genres=without_genres, without_keywords=without_keywords, without_watch_providers=without_watch_providers, year=year)

Movie

Find movies using over 30 filters and sort options.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.discover_movie200_response import DiscoverMovie200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    certification = 'certification_example' # str | use in conjunction with `region` (optional)
    certification_gte = 'certification_gte_example' # str | use in conjunction with `region` (optional)
    certification_lte = 'certification_lte_example' # str | use in conjunction with `region` (optional)
    certification_country = 'certification_country_example' # str | use in conjunction with the `certification`, `certification.gte` and `certification.lte` filters (optional)
    include_adult = False # bool |  (optional) (default to False)
    include_video = False # bool |  (optional) (default to False)
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)
    primary_release_year = 56 # int |  (optional)
    primary_release_date_gte = '2013-10-20' # date |  (optional)
    primary_release_date_lte = '2013-10-20' # date |  (optional)
    region = 'region_example' # str |  (optional)
    release_date_gte = '2013-10-20' # date |  (optional)
    release_date_lte = '2013-10-20' # date |  (optional)
    sort_by = 'popularity.desc' # str |  (optional) (default to 'popularity.desc')
    vote_average_gte = 3.4 # float |  (optional)
    vote_average_lte = 3.4 # float |  (optional)
    vote_count_gte = 3.4 # float |  (optional)
    vote_count_lte = 3.4 # float |  (optional)
    watch_region = 'watch_region_example' # str | use in conjunction with `with_watch_monetization_types ` or `with_watch_providers ` (optional)
    with_cast = 'with_cast_example' # str | can be a comma (`AND`) or pipe (`OR`) separated query (optional)
    with_companies = 'with_companies_example' # str | can be a comma (`AND`) or pipe (`OR`) separated query (optional)
    with_crew = 'with_crew_example' # str | can be a comma (`AND`) or pipe (`OR`) separated query (optional)
    with_genres = 'with_genres_example' # str | can be a comma (`AND`) or pipe (`OR`) separated query (optional)
    with_keywords = 'with_keywords_example' # str | can be a comma (`AND`) or pipe (`OR`) separated query (optional)
    with_origin_country = 'with_origin_country_example' # str |  (optional)
    with_original_language = 'with_original_language_example' # str |  (optional)
    with_people = 'with_people_example' # str | can be a comma (`AND`) or pipe (`OR`) separated query (optional)
    with_release_type = 56 # int | possible values are: [1, 2, 3, 4, 5, 6] can be a comma (`AND`) or pipe (`OR`) separated query, can be used in conjunction with `region` (optional)
    with_runtime_gte = 56 # int |  (optional)
    with_runtime_lte = 56 # int |  (optional)
    with_watch_monetization_types = 'with_watch_monetization_types_example' # str | possible values are: [flatrate, free, ads, rent, buy] use in conjunction with `watch_region`, can be a comma (`AND`) or pipe (`OR`) separated query (optional)
    with_watch_providers = 'with_watch_providers_example' # str | use in conjunction with `watch_region`, can be a comma (`AND`) or pipe (`OR`) separated query (optional)
    without_companies = 'without_companies_example' # str |  (optional)
    without_genres = 'without_genres_example' # str |  (optional)
    without_keywords = 'without_keywords_example' # str |  (optional)
    without_watch_providers = 'without_watch_providers_example' # str |  (optional)
    year = 56 # int |  (optional)

    try:
        # Movie
        api_response = api_instance.discover_movie(certification=certification, certification_gte=certification_gte, certification_lte=certification_lte, certification_country=certification_country, include_adult=include_adult, include_video=include_video, language=language, page=page, primary_release_year=primary_release_year, primary_release_date_gte=primary_release_date_gte, primary_release_date_lte=primary_release_date_lte, region=region, release_date_gte=release_date_gte, release_date_lte=release_date_lte, sort_by=sort_by, vote_average_gte=vote_average_gte, vote_average_lte=vote_average_lte, vote_count_gte=vote_count_gte, vote_count_lte=vote_count_lte, watch_region=watch_region, with_cast=with_cast, with_companies=with_companies, with_crew=with_crew, with_genres=with_genres, with_keywords=with_keywords, with_origin_country=with_origin_country, with_original_language=with_original_language, with_people=with_people, with_release_type=with_release_type, with_runtime_gte=with_runtime_gte, with_runtime_lte=with_runtime_lte, with_watch_monetization_types=with_watch_monetization_types, with_watch_providers=with_watch_providers, without_companies=without_companies, without_genres=without_genres, without_keywords=without_keywords, without_watch_providers=without_watch_providers, year=year)
        print("The response of DefaultApi->discover_movie:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->discover_movie: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certification** | **str**| use in conjunction with &#x60;region&#x60; | [optional] 
 **certification_gte** | **str**| use in conjunction with &#x60;region&#x60; | [optional] 
 **certification_lte** | **str**| use in conjunction with &#x60;region&#x60; | [optional] 
 **certification_country** | **str**| use in conjunction with the &#x60;certification&#x60;, &#x60;certification.gte&#x60; and &#x60;certification.lte&#x60; filters | [optional] 
 **include_adult** | **bool**|  | [optional] [default to False]
 **include_video** | **bool**|  | [optional] [default to False]
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]
 **primary_release_year** | **int**|  | [optional] 
 **primary_release_date_gte** | **date**|  | [optional] 
 **primary_release_date_lte** | **date**|  | [optional] 
 **region** | **str**|  | [optional] 
 **release_date_gte** | **date**|  | [optional] 
 **release_date_lte** | **date**|  | [optional] 
 **sort_by** | **str**|  | [optional] [default to &#39;popularity.desc&#39;]
 **vote_average_gte** | **float**|  | [optional] 
 **vote_average_lte** | **float**|  | [optional] 
 **vote_count_gte** | **float**|  | [optional] 
 **vote_count_lte** | **float**|  | [optional] 
 **watch_region** | **str**| use in conjunction with &#x60;with_watch_monetization_types &#x60; or &#x60;with_watch_providers &#x60; | [optional] 
 **with_cast** | **str**| can be a comma (&#x60;AND&#x60;) or pipe (&#x60;OR&#x60;) separated query | [optional] 
 **with_companies** | **str**| can be a comma (&#x60;AND&#x60;) or pipe (&#x60;OR&#x60;) separated query | [optional] 
 **with_crew** | **str**| can be a comma (&#x60;AND&#x60;) or pipe (&#x60;OR&#x60;) separated query | [optional] 
 **with_genres** | **str**| can be a comma (&#x60;AND&#x60;) or pipe (&#x60;OR&#x60;) separated query | [optional] 
 **with_keywords** | **str**| can be a comma (&#x60;AND&#x60;) or pipe (&#x60;OR&#x60;) separated query | [optional] 
 **with_origin_country** | **str**|  | [optional] 
 **with_original_language** | **str**|  | [optional] 
 **with_people** | **str**| can be a comma (&#x60;AND&#x60;) or pipe (&#x60;OR&#x60;) separated query | [optional] 
 **with_release_type** | **int**| possible values are: [1, 2, 3, 4, 5, 6] can be a comma (&#x60;AND&#x60;) or pipe (&#x60;OR&#x60;) separated query, can be used in conjunction with &#x60;region&#x60; | [optional] 
 **with_runtime_gte** | **int**|  | [optional] 
 **with_runtime_lte** | **int**|  | [optional] 
 **with_watch_monetization_types** | **str**| possible values are: [flatrate, free, ads, rent, buy] use in conjunction with &#x60;watch_region&#x60;, can be a comma (&#x60;AND&#x60;) or pipe (&#x60;OR&#x60;) separated query | [optional] 
 **with_watch_providers** | **str**| use in conjunction with &#x60;watch_region&#x60;, can be a comma (&#x60;AND&#x60;) or pipe (&#x60;OR&#x60;) separated query | [optional] 
 **without_companies** | **str**|  | [optional] 
 **without_genres** | **str**|  | [optional] 
 **without_keywords** | **str**|  | [optional] 
 **without_watch_providers** | **str**|  | [optional] 
 **year** | **int**|  | [optional] 

### Return type

[**DiscoverMovie200Response**](DiscoverMovie200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_tv**
> DiscoverTv200Response discover_tv(air_date_gte=air_date_gte, air_date_lte=air_date_lte, first_air_date_year=first_air_date_year, first_air_date_gte=first_air_date_gte, first_air_date_lte=first_air_date_lte, include_adult=include_adult, include_null_first_air_dates=include_null_first_air_dates, language=language, page=page, screened_theatrically=screened_theatrically, sort_by=sort_by, timezone=timezone, vote_average_gte=vote_average_gte, vote_average_lte=vote_average_lte, vote_count_gte=vote_count_gte, vote_count_lte=vote_count_lte, watch_region=watch_region, with_companies=with_companies, with_genres=with_genres, with_keywords=with_keywords, with_networks=with_networks, with_origin_country=with_origin_country, with_original_language=with_original_language, with_runtime_gte=with_runtime_gte, with_runtime_lte=with_runtime_lte, with_status=with_status, with_watch_monetization_types=with_watch_monetization_types, with_watch_providers=with_watch_providers, without_companies=without_companies, without_genres=without_genres, without_keywords=without_keywords, without_watch_providers=without_watch_providers, with_type=with_type)

TV

Find TV shows using over 30 filters and sort options.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.discover_tv200_response import DiscoverTv200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    air_date_gte = '2013-10-20' # date |  (optional)
    air_date_lte = '2013-10-20' # date |  (optional)
    first_air_date_year = 56 # int |  (optional)
    first_air_date_gte = '2013-10-20' # date |  (optional)
    first_air_date_lte = '2013-10-20' # date |  (optional)
    include_adult = False # bool |  (optional) (default to False)
    include_null_first_air_dates = False # bool |  (optional) (default to False)
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)
    screened_theatrically = True # bool |  (optional)
    sort_by = 'popularity.desc' # str |  (optional) (default to 'popularity.desc')
    timezone = 'timezone_example' # str |  (optional)
    vote_average_gte = 3.4 # float |  (optional)
    vote_average_lte = 3.4 # float |  (optional)
    vote_count_gte = 3.4 # float |  (optional)
    vote_count_lte = 3.4 # float |  (optional)
    watch_region = 'watch_region_example' # str | use in conjunction with `with_watch_monetization_types ` or `with_watch_providers ` (optional)
    with_companies = 'with_companies_example' # str | can be a comma (`AND`) or pipe (`OR`) separated query (optional)
    with_genres = 'with_genres_example' # str | can be a comma (`AND`) or pipe (`OR`) separated query (optional)
    with_keywords = 'with_keywords_example' # str | can be a comma (`AND`) or pipe (`OR`) separated query (optional)
    with_networks = 56 # int |  (optional)
    with_origin_country = 'with_origin_country_example' # str |  (optional)
    with_original_language = 'with_original_language_example' # str |  (optional)
    with_runtime_gte = 56 # int |  (optional)
    with_runtime_lte = 56 # int |  (optional)
    with_status = 'with_status_example' # str | possible values are: [0, 1, 2, 3, 4, 5], can be a comma (`AND`) or pipe (`OR`) separated query (optional)
    with_watch_monetization_types = 'with_watch_monetization_types_example' # str | possible values are: [flatrate, free, ads, rent, buy] use in conjunction with `watch_region`, can be a comma (`AND`) or pipe (`OR`) separated query (optional)
    with_watch_providers = 'with_watch_providers_example' # str | use in conjunction with `watch_region`, can be a comma (`AND`) or pipe (`OR`) separated query (optional)
    without_companies = 'without_companies_example' # str |  (optional)
    without_genres = 'without_genres_example' # str |  (optional)
    without_keywords = 'without_keywords_example' # str |  (optional)
    without_watch_providers = 'without_watch_providers_example' # str |  (optional)
    with_type = 'with_type_example' # str | possible values are: [0, 1, 2, 3, 4, 5, 6], can be a comma (`AND`) or pipe (`OR`) separated query (optional)

    try:
        # TV
        api_response = api_instance.discover_tv(air_date_gte=air_date_gte, air_date_lte=air_date_lte, first_air_date_year=first_air_date_year, first_air_date_gte=first_air_date_gte, first_air_date_lte=first_air_date_lte, include_adult=include_adult, include_null_first_air_dates=include_null_first_air_dates, language=language, page=page, screened_theatrically=screened_theatrically, sort_by=sort_by, timezone=timezone, vote_average_gte=vote_average_gte, vote_average_lte=vote_average_lte, vote_count_gte=vote_count_gte, vote_count_lte=vote_count_lte, watch_region=watch_region, with_companies=with_companies, with_genres=with_genres, with_keywords=with_keywords, with_networks=with_networks, with_origin_country=with_origin_country, with_original_language=with_original_language, with_runtime_gte=with_runtime_gte, with_runtime_lte=with_runtime_lte, with_status=with_status, with_watch_monetization_types=with_watch_monetization_types, with_watch_providers=with_watch_providers, without_companies=without_companies, without_genres=without_genres, without_keywords=without_keywords, without_watch_providers=without_watch_providers, with_type=with_type)
        print("The response of DefaultApi->discover_tv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->discover_tv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **air_date_gte** | **date**|  | [optional] 
 **air_date_lte** | **date**|  | [optional] 
 **first_air_date_year** | **int**|  | [optional] 
 **first_air_date_gte** | **date**|  | [optional] 
 **first_air_date_lte** | **date**|  | [optional] 
 **include_adult** | **bool**|  | [optional] [default to False]
 **include_null_first_air_dates** | **bool**|  | [optional] [default to False]
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]
 **screened_theatrically** | **bool**|  | [optional] 
 **sort_by** | **str**|  | [optional] [default to &#39;popularity.desc&#39;]
 **timezone** | **str**|  | [optional] 
 **vote_average_gte** | **float**|  | [optional] 
 **vote_average_lte** | **float**|  | [optional] 
 **vote_count_gte** | **float**|  | [optional] 
 **vote_count_lte** | **float**|  | [optional] 
 **watch_region** | **str**| use in conjunction with &#x60;with_watch_monetization_types &#x60; or &#x60;with_watch_providers &#x60; | [optional] 
 **with_companies** | **str**| can be a comma (&#x60;AND&#x60;) or pipe (&#x60;OR&#x60;) separated query | [optional] 
 **with_genres** | **str**| can be a comma (&#x60;AND&#x60;) or pipe (&#x60;OR&#x60;) separated query | [optional] 
 **with_keywords** | **str**| can be a comma (&#x60;AND&#x60;) or pipe (&#x60;OR&#x60;) separated query | [optional] 
 **with_networks** | **int**|  | [optional] 
 **with_origin_country** | **str**|  | [optional] 
 **with_original_language** | **str**|  | [optional] 
 **with_runtime_gte** | **int**|  | [optional] 
 **with_runtime_lte** | **int**|  | [optional] 
 **with_status** | **str**| possible values are: [0, 1, 2, 3, 4, 5], can be a comma (&#x60;AND&#x60;) or pipe (&#x60;OR&#x60;) separated query | [optional] 
 **with_watch_monetization_types** | **str**| possible values are: [flatrate, free, ads, rent, buy] use in conjunction with &#x60;watch_region&#x60;, can be a comma (&#x60;AND&#x60;) or pipe (&#x60;OR&#x60;) separated query | [optional] 
 **with_watch_providers** | **str**| use in conjunction with &#x60;watch_region&#x60;, can be a comma (&#x60;AND&#x60;) or pipe (&#x60;OR&#x60;) separated query | [optional] 
 **without_companies** | **str**|  | [optional] 
 **without_genres** | **str**|  | [optional] 
 **without_keywords** | **str**|  | [optional] 
 **without_watch_providers** | **str**|  | [optional] 
 **with_type** | **str**| possible values are: [0, 1, 2, 3, 4, 5, 6], can be a comma (&#x60;AND&#x60;) or pipe (&#x60;OR&#x60;) separated query | [optional] 

### Return type

[**DiscoverTv200Response**](DiscoverTv200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_id**
> FindById200Response find_by_id(external_id, external_source, language=language)

Find By ID

Find data by external ID's.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.find_by_id200_response import FindById200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    external_id = 'external_id_example' # str | 
    external_source = 'external_source_example' # str | 
    language = 'language_example' # str |  (optional)

    try:
        # Find By ID
        api_response = api_instance.find_by_id(external_id, external_source, language=language)
        print("The response of DefaultApi->find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  | 
 **external_source** | **str**|  | 
 **language** | **str**|  | [optional] 

### Return type

[**FindById200Response**](FindById200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genre_movie_list**
> GenreMovieList200Response genre_movie_list(language=language)

Movie List

Get the list of official genres for movies.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.genre_movie_list200_response import GenreMovieList200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    language = 'en' # str |  (optional) (default to 'en')

    try:
        # Movie List
        api_response = api_instance.genre_movie_list(language=language)
        print("The response of DefaultApi->genre_movie_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->genre_movie_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | [optional] [default to &#39;en&#39;]

### Return type

[**GenreMovieList200Response**](GenreMovieList200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genre_tv_list**
> GenreTvList200Response genre_tv_list(language=language)

TV List

Get the list of official genres for TV shows.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.genre_tv_list200_response import GenreTvList200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    language = 'en' # str |  (optional) (default to 'en')

    try:
        # TV List
        api_response = api_instance.genre_tv_list(language=language)
        print("The response of DefaultApi->genre_tv_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->genre_tv_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | [optional] [default to &#39;en&#39;]

### Return type

[**GenreTvList200Response**](GenreTvList200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_session_rated_movies**
> GuestSessionRatedMovies200Response guest_session_rated_movies(guest_session_id, language=language, page=page, sort_by=sort_by)

Rated Movies

Get the rated movies for a guest session.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.guest_session_rated_movies200_response import GuestSessionRatedMovies200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    guest_session_id = 'guest_session_id_example' # str | 
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)
    sort_by = 'created_at.asc' # str |  (optional) (default to 'created_at.asc')

    try:
        # Rated Movies
        api_response = api_instance.guest_session_rated_movies(guest_session_id, language=language, page=page, sort_by=sort_by)
        print("The response of DefaultApi->guest_session_rated_movies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->guest_session_rated_movies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guest_session_id** | **str**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]
 **sort_by** | **str**|  | [optional] [default to &#39;created_at.asc&#39;]

### Return type

[**GuestSessionRatedMovies200Response**](GuestSessionRatedMovies200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_session_rated_tv**
> GuestSessionRatedTv200Response guest_session_rated_tv(guest_session_id, language=language, page=page, sort_by=sort_by)

Rated TV

Get the rated TV shows for a guest session.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.guest_session_rated_tv200_response import GuestSessionRatedTv200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    guest_session_id = 'guest_session_id_example' # str | 
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)
    sort_by = 'created_at.asc' # str |  (optional) (default to 'created_at.asc')

    try:
        # Rated TV
        api_response = api_instance.guest_session_rated_tv(guest_session_id, language=language, page=page, sort_by=sort_by)
        print("The response of DefaultApi->guest_session_rated_tv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->guest_session_rated_tv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guest_session_id** | **str**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]
 **sort_by** | **str**|  | [optional] [default to &#39;created_at.asc&#39;]

### Return type

[**GuestSessionRatedTv200Response**](GuestSessionRatedTv200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guest_session_rated_tv_episodes**
> GuestSessionRatedTvEpisodes200Response guest_session_rated_tv_episodes(guest_session_id, language=language, page=page, sort_by=sort_by)

Rated TV Episodes

Get the rated TV episodes for a guest session.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.guest_session_rated_tv_episodes200_response import GuestSessionRatedTvEpisodes200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    guest_session_id = 'guest_session_id_example' # str | 
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)
    sort_by = 'created_at.asc' # str |  (optional) (default to 'created_at.asc')

    try:
        # Rated TV Episodes
        api_response = api_instance.guest_session_rated_tv_episodes(guest_session_id, language=language, page=page, sort_by=sort_by)
        print("The response of DefaultApi->guest_session_rated_tv_episodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->guest_session_rated_tv_episodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guest_session_id** | **str**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]
 **sort_by** | **str**|  | [optional] [default to &#39;created_at.asc&#39;]

### Return type

[**GuestSessionRatedTvEpisodes200Response**](GuestSessionRatedTvEpisodes200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keyword_details**
> KeywordDetails200Response keyword_details(keyword_id)

Details



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.keyword_details200_response import KeywordDetails200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    keyword_id = 56 # int | 

    try:
        # Details
        api_response = api_instance.keyword_details(keyword_id)
        print("The response of DefaultApi->keyword_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->keyword_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword_id** | **int**|  | 

### Return type

[**KeywordDetails200Response**](KeywordDetails200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keyword_movies**
> KeywordMovies200Response keyword_movies(keyword_id, include_adult=include_adult, language=language, page=page)

Movies



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.keyword_movies200_response import KeywordMovies200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    keyword_id = 'keyword_id_example' # str | 
    include_adult = False # bool |  (optional) (default to False)
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)

    try:
        # Movies
        api_response = api_instance.keyword_movies(keyword_id, include_adult=include_adult, language=language, page=page)
        print("The response of DefaultApi->keyword_movies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->keyword_movies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword_id** | **str**|  | 
 **include_adult** | **bool**|  | [optional] [default to False]
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]

### Return type

[**KeywordMovies200Response**](KeywordMovies200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_add_movie**
> ListDelete200Response list_add_movie(list_id, session_id, list_add_movie_request=list_add_movie_request)

Add Movie

Add a movie to a list.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.list_add_movie_request import ListAddMovieRequest
from openapi_client.models.list_delete200_response import ListDelete200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    list_id = 56 # int | 
    session_id = 'session_id_example' # str | 
    list_add_movie_request = {"media_id":18} # ListAddMovieRequest |  (optional)

    try:
        # Add Movie
        api_response = api_instance.list_add_movie(list_id, session_id, list_add_movie_request=list_add_movie_request)
        print("The response of DefaultApi->list_add_movie:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_add_movie: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**|  | 
 **session_id** | **str**|  | 
 **list_add_movie_request** | [**ListAddMovieRequest**](ListAddMovieRequest.md)|  | [optional] 

### Return type

[**ListDelete200Response**](ListDelete200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_check_item_status**
> ListCheckItemStatus200Response list_check_item_status(list_id, language=language, movie_id=movie_id)

Check Item Status

Use this method to check if an item has already been added to the list.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.list_check_item_status200_response import ListCheckItemStatus200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    list_id = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')
    movie_id = 56 # int |  (optional)

    try:
        # Check Item Status
        api_response = api_instance.list_check_item_status(list_id, language=language, movie_id=movie_id)
        print("The response of DefaultApi->list_check_item_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_check_item_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **movie_id** | **int**|  | [optional] 

### Return type

[**ListCheckItemStatus200Response**](ListCheckItemStatus200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_clear**
> ListDelete200Response list_clear(list_id, session_id, confirm)

Clear

Clear all items from a list.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.list_delete200_response import ListDelete200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    list_id = 56 # int | 
    session_id = 'session_id_example' # str | 
    confirm = False # bool |  (default to False)

    try:
        # Clear
        api_response = api_instance.list_clear(list_id, session_id, confirm)
        print("The response of DefaultApi->list_clear:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_clear: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**|  | 
 **session_id** | **str**|  | 
 **confirm** | **bool**|  | [default to False]

### Return type

[**ListDelete200Response**](ListDelete200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_create**
> ListCreate200Response list_create(session_id, movie_add_rating_request=movie_add_rating_request)

Create



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.list_create200_response import ListCreate200Response
from openapi_client.models.movie_add_rating_request import MovieAddRatingRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    session_id = 'session_id_example' # str | 
    movie_add_rating_request = {"name":"This is my awesome test list.","description":"Just an awesome list.","language":"en"} # MovieAddRatingRequest |  (optional)

    try:
        # Create
        api_response = api_instance.list_create(session_id, movie_add_rating_request=movie_add_rating_request)
        print("The response of DefaultApi->list_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **movie_add_rating_request** | [**MovieAddRatingRequest**](MovieAddRatingRequest.md)|  | [optional] 

### Return type

[**ListCreate200Response**](ListCreate200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_delete**
> ListDelete200Response list_delete(list_id, session_id)

Delete

Delete a list.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.list_delete200_response import ListDelete200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    list_id = 56 # int | 
    session_id = 'session_id_example' # str | 

    try:
        # Delete
        api_response = api_instance.list_delete(list_id, session_id)
        print("The response of DefaultApi->list_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**|  | 
 **session_id** | **str**|  | 

### Return type

[**ListDelete200Response**](ListDelete200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_details**
> ListDetails200Response list_details(list_id, language=language, page=page)

Details



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.list_details200_response import ListDetails200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    list_id = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)

    try:
        # Details
        api_response = api_instance.list_details(list_id, language=language, page=page)
        print("The response of DefaultApi->list_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]

### Return type

[**ListDetails200Response**](ListDetails200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_remove_movie**
> MovieDeleteRating200Response list_remove_movie(list_id, session_id, movie_add_rating_request=movie_add_rating_request)

Remove Movie

Remove a movie from a list.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_add_rating_request import MovieAddRatingRequest
from openapi_client.models.movie_delete_rating200_response import MovieDeleteRating200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    list_id = 56 # int | 
    session_id = 'session_id_example' # str | 
    movie_add_rating_request = {media_id=18} # MovieAddRatingRequest |  (optional)

    try:
        # Remove Movie
        api_response = api_instance.list_remove_movie(list_id, session_id, movie_add_rating_request=movie_add_rating_request)
        print("The response of DefaultApi->list_remove_movie:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_remove_movie: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**|  | 
 **session_id** | **str**|  | 
 **movie_add_rating_request** | [**MovieAddRatingRequest**](MovieAddRatingRequest.md)|  | [optional] 

### Return type

[**MovieDeleteRating200Response**](MovieDeleteRating200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_copy**
> ListsCopy200Response lists_copy(series_id, language=language, page=page)

Lists

Get the lists that a TV series has been added to.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.lists_copy200_response import ListsCopy200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)

    try:
        # Lists
        api_response = api_instance.lists_copy(series_id, language=language, page=page)
        print("The response of DefaultApi->lists_copy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->lists_copy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]

### Return type

[**ListsCopy200Response**](ListsCopy200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **movie_account_states**
> MovieAccountStates200Response movie_account_states(movie_id, session_id=session_id, guest_session_id=guest_session_id)

Account States

Get the rating, watchlist and favourite status of an account.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_account_states200_response import MovieAccountStates200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    movie_id = 56 # int | 
    session_id = 'session_id_example' # str |  (optional)
    guest_session_id = 'guest_session_id_example' # str |  (optional)

    try:
        # Account States
        api_response = api_instance.movie_account_states(movie_id, session_id=session_id, guest_session_id=guest_session_id)
        print("The response of DefaultApi->movie_account_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->movie_account_states: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **int**|  | 
 **session_id** | **str**|  | [optional] 
 **guest_session_id** | **str**|  | [optional] 

### Return type

[**MovieAccountStates200Response**](MovieAccountStates200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **movie_add_rating**
> MovieAddRating200Response movie_add_rating(movie_id, content_type, guest_session_id=guest_session_id, session_id=session_id, movie_add_rating_request=movie_add_rating_request)

Add Rating

Rate a movie and save it to your rated list.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_add_rating200_response import MovieAddRating200Response
from openapi_client.models.movie_add_rating_request import MovieAddRatingRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    movie_id = 56 # int | 
    content_type = 'application/json;charset=utf-8' # str |  (default to 'application/json;charset=utf-8')
    guest_session_id = 'guest_session_id_example' # str |  (optional)
    session_id = 'session_id_example' # str |  (optional)
    movie_add_rating_request = {"value":8.5} # MovieAddRatingRequest |  (optional)

    try:
        # Add Rating
        api_response = api_instance.movie_add_rating(movie_id, content_type, guest_session_id=guest_session_id, session_id=session_id, movie_add_rating_request=movie_add_rating_request)
        print("The response of DefaultApi->movie_add_rating:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->movie_add_rating: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **int**|  | 
 **content_type** | **str**|  | [default to &#39;application/json;charset&#x3D;utf-8&#39;]
 **guest_session_id** | **str**|  | [optional] 
 **session_id** | **str**|  | [optional] 
 **movie_add_rating_request** | [**MovieAddRatingRequest**](MovieAddRatingRequest.md)|  | [optional] 

### Return type

[**MovieAddRating200Response**](MovieAddRating200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **movie_alternative_titles**
> MovieAlternativeTitles200Response movie_alternative_titles(movie_id, country=country)

Alternative Titles

Get the alternative titles for a movie.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_alternative_titles200_response import MovieAlternativeTitles200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    movie_id = 56 # int | 
    country = 'country_example' # str | specify a ISO-3166-1 value to filter the results (optional)

    try:
        # Alternative Titles
        api_response = api_instance.movie_alternative_titles(movie_id, country=country)
        print("The response of DefaultApi->movie_alternative_titles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->movie_alternative_titles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **int**|  | 
 **country** | **str**| specify a ISO-3166-1 value to filter the results | [optional] 

### Return type

[**MovieAlternativeTitles200Response**](MovieAlternativeTitles200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **movie_changes**
> MovieChanges200Response movie_changes(movie_id, end_date=end_date, page=page, start_date=start_date)

Changes

Get the recent changes for a movie.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_changes200_response import MovieChanges200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    movie_id = 56 # int | 
    end_date = '2013-10-20' # date |  (optional)
    page = 1 # int |  (optional) (default to 1)
    start_date = '2013-10-20' # date |  (optional)

    try:
        # Changes
        api_response = api_instance.movie_changes(movie_id, end_date=end_date, page=page, start_date=start_date)
        print("The response of DefaultApi->movie_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->movie_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **int**|  | 
 **end_date** | **date**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **start_date** | **date**|  | [optional] 

### Return type

[**MovieChanges200Response**](MovieChanges200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **movie_credits**
> MovieCredits200Response movie_credits(movie_id, language=language)

Credits



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_credits200_response import MovieCredits200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    movie_id = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Credits
        api_response = api_instance.movie_credits(movie_id, language=language)
        print("The response of DefaultApi->movie_credits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->movie_credits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**MovieCredits200Response**](MovieCredits200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **movie_delete_rating**
> MovieDeleteRating200Response movie_delete_rating(movie_id, content_type=content_type, guest_session_id=guest_session_id, session_id=session_id)

Delete Rating

Delete a user rating.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_delete_rating200_response import MovieDeleteRating200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    movie_id = 56 # int | 
    content_type = 'application/json;charset=utf-8' # str |  (optional) (default to 'application/json;charset=utf-8')
    guest_session_id = 'guest_session_id_example' # str |  (optional)
    session_id = 'session_id_example' # str |  (optional)

    try:
        # Delete Rating
        api_response = api_instance.movie_delete_rating(movie_id, content_type=content_type, guest_session_id=guest_session_id, session_id=session_id)
        print("The response of DefaultApi->movie_delete_rating:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->movie_delete_rating: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **int**|  | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json;charset&#x3D;utf-8&#39;]
 **guest_session_id** | **str**|  | [optional] 
 **session_id** | **str**|  | [optional] 

### Return type

[**MovieDeleteRating200Response**](MovieDeleteRating200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **movie_details**
> MovieDetails200Response movie_details(movie_id, append_to_response=append_to_response, language=language)

Details

Get the top level details of a movie by ID.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_details200_response import MovieDetails200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    movie_id = 56 # int | 
    append_to_response = 'append_to_response_example' # str | comma separated list of endpoints within this namespace, 20 items max (optional)
    language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Details
        api_response = api_instance.movie_details(movie_id, append_to_response=append_to_response, language=language)
        print("The response of DefaultApi->movie_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->movie_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **int**|  | 
 **append_to_response** | **str**| comma separated list of endpoints within this namespace, 20 items max | [optional] 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**MovieDetails200Response**](MovieDetails200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **movie_external_ids**
> MovieExternalIds200Response movie_external_ids(movie_id)

External IDs



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_external_ids200_response import MovieExternalIds200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    movie_id = 56 # int | 

    try:
        # External IDs
        api_response = api_instance.movie_external_ids(movie_id)
        print("The response of DefaultApi->movie_external_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->movie_external_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **int**|  | 

### Return type

[**MovieExternalIds200Response**](MovieExternalIds200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **movie_images**
> MovieImages200Response movie_images(movie_id, include_image_language=include_image_language, language=language)

Images

Get the images that belong to a movie.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_images200_response import MovieImages200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    movie_id = 56 # int | 
    include_image_language = 'include_image_language_example' # str | specify a comma separated list of ISO-639-1 values to query, for example: `en,null` (optional)
    language = 'language_example' # str |  (optional)

    try:
        # Images
        api_response = api_instance.movie_images(movie_id, include_image_language=include_image_language, language=language)
        print("The response of DefaultApi->movie_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->movie_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **int**|  | 
 **include_image_language** | **str**| specify a comma separated list of ISO-639-1 values to query, for example: &#x60;en,null&#x60; | [optional] 
 **language** | **str**|  | [optional] 

### Return type

[**MovieImages200Response**](MovieImages200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **movie_keywords**
> MovieKeywords200Response movie_keywords(movie_id)

Keywords



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_keywords200_response import MovieKeywords200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    movie_id = 'movie_id_example' # str | 

    try:
        # Keywords
        api_response = api_instance.movie_keywords(movie_id)
        print("The response of DefaultApi->movie_keywords:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->movie_keywords: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **str**|  | 

### Return type

[**MovieKeywords200Response**](MovieKeywords200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **movie_latest_id**
> MovieLatestId200Response movie_latest_id()

Latest

Get the newest movie ID.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_latest_id200_response import MovieLatestId200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Latest
        api_response = api_instance.movie_latest_id()
        print("The response of DefaultApi->movie_latest_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->movie_latest_id: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MovieLatestId200Response**](MovieLatestId200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **movie_lists**
> MovieLists200Response movie_lists(movie_id, language=language, page=page)

Lists

Get the lists that a movie has been added to.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_lists200_response import MovieLists200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    movie_id = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)

    try:
        # Lists
        api_response = api_instance.movie_lists(movie_id, language=language, page=page)
        print("The response of DefaultApi->movie_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->movie_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]

### Return type

[**MovieLists200Response**](MovieLists200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **movie_now_playing_list**
> MovieNowPlayingList200Response movie_now_playing_list(language=language, page=page, region=region)

Now Playing

Get a list of movies that are currently in theatres.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_now_playing_list200_response import MovieNowPlayingList200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)
    region = 'region_example' # str | ISO-3166-1 code (optional)

    try:
        # Now Playing
        api_response = api_instance.movie_now_playing_list(language=language, page=page, region=region)
        print("The response of DefaultApi->movie_now_playing_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->movie_now_playing_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]
 **region** | **str**| ISO-3166-1 code | [optional] 

### Return type

[**MovieNowPlayingList200Response**](MovieNowPlayingList200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **movie_popular_list**
> MoviePopularList200Response movie_popular_list(language=language, page=page, region=region)

Popular

Get a list of movies ordered by popularity.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_popular_list200_response import MoviePopularList200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)
    region = 'region_example' # str | ISO-3166-1 code (optional)

    try:
        # Popular
        api_response = api_instance.movie_popular_list(language=language, page=page, region=region)
        print("The response of DefaultApi->movie_popular_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->movie_popular_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]
 **region** | **str**| ISO-3166-1 code | [optional] 

### Return type

[**MoviePopularList200Response**](MoviePopularList200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **movie_recommendations**
> object movie_recommendations(movie_id, language=language, page=page)

Recommendations



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    movie_id = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)

    try:
        # Recommendations
        api_response = api_instance.movie_recommendations(movie_id, language=language, page=page)
        print("The response of DefaultApi->movie_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->movie_recommendations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]

### Return type

**object**

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **movie_release_dates**
> MovieReleaseDates200Response movie_release_dates(movie_id)

Release Dates

Get the release dates and certifications for a movie.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_release_dates200_response import MovieReleaseDates200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    movie_id = 56 # int | 

    try:
        # Release Dates
        api_response = api_instance.movie_release_dates(movie_id)
        print("The response of DefaultApi->movie_release_dates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->movie_release_dates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **int**|  | 

### Return type

[**MovieReleaseDates200Response**](MovieReleaseDates200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **movie_reviews**
> MovieReviews200Response movie_reviews(movie_id, language=language, page=page)

Reviews

Get the user reviews for a movie.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_reviews200_response import MovieReviews200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    movie_id = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)

    try:
        # Reviews
        api_response = api_instance.movie_reviews(movie_id, language=language, page=page)
        print("The response of DefaultApi->movie_reviews:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->movie_reviews: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]

### Return type

[**MovieReviews200Response**](MovieReviews200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **movie_similar**
> MovieSimilar200Response movie_similar(movie_id, language=language, page=page)

Similar

Get the similar movies based on genres and keywords.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_similar200_response import MovieSimilar200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    movie_id = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)

    try:
        # Similar
        api_response = api_instance.movie_similar(movie_id, language=language, page=page)
        print("The response of DefaultApi->movie_similar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->movie_similar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]

### Return type

[**MovieSimilar200Response**](MovieSimilar200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **movie_top_rated_list**
> MovieTopRatedList200Response movie_top_rated_list(language=language, page=page, region=region)

Top Rated

Get a list of movies ordered by rating.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_top_rated_list200_response import MovieTopRatedList200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)
    region = 'region_example' # str | ISO-3166-1 code (optional)

    try:
        # Top Rated
        api_response = api_instance.movie_top_rated_list(language=language, page=page, region=region)
        print("The response of DefaultApi->movie_top_rated_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->movie_top_rated_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]
 **region** | **str**| ISO-3166-1 code | [optional] 

### Return type

[**MovieTopRatedList200Response**](MovieTopRatedList200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **movie_translations**
> MovieTranslations200Response movie_translations(movie_id)

Translations

Get the translations for a movie.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_translations200_response import MovieTranslations200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    movie_id = 56 # int | 

    try:
        # Translations
        api_response = api_instance.movie_translations(movie_id)
        print("The response of DefaultApi->movie_translations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->movie_translations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **int**|  | 

### Return type

[**MovieTranslations200Response**](MovieTranslations200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **movie_upcoming_list**
> MovieUpcomingList200Response movie_upcoming_list(language=language, page=page, region=region)

Upcoming

Get a list of movies that are being released soon.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_upcoming_list200_response import MovieUpcomingList200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)
    region = 'region_example' # str | ISO-3166-1 code (optional)

    try:
        # Upcoming
        api_response = api_instance.movie_upcoming_list(language=language, page=page, region=region)
        print("The response of DefaultApi->movie_upcoming_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->movie_upcoming_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]
 **region** | **str**| ISO-3166-1 code | [optional] 

### Return type

[**MovieUpcomingList200Response**](MovieUpcomingList200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **movie_videos**
> MovieVideos200Response movie_videos(movie_id, language=language)

Videos



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_videos200_response import MovieVideos200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    movie_id = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Videos
        api_response = api_instance.movie_videos(movie_id, language=language)
        print("The response of DefaultApi->movie_videos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->movie_videos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**MovieVideos200Response**](MovieVideos200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **movie_watch_providers**
> MovieWatchProviders200Response movie_watch_providers(movie_id)

Watch Providers

Get the list of streaming providers we have for a movie.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_watch_providers200_response import MovieWatchProviders200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    movie_id = 56 # int | 

    try:
        # Watch Providers
        api_response = api_instance.movie_watch_providers(movie_id)
        print("The response of DefaultApi->movie_watch_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->movie_watch_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **int**|  | 

### Return type

[**MovieWatchProviders200Response**](MovieWatchProviders200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_details**
> NetworkDetails200Response network_details(network_id)

Details



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.network_details200_response import NetworkDetails200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    network_id = 56 # int | 

    try:
        # Details
        api_response = api_instance.network_details(network_id)
        print("The response of DefaultApi->network_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->network_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **int**|  | 

### Return type

[**NetworkDetails200Response**](NetworkDetails200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **person_changes**
> PersonChanges200Response person_changes(person_id, end_date=end_date, page=page, start_date=start_date)

Changes

Get the recent changes for a person.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.person_changes200_response import PersonChanges200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    person_id = 56 # int | 
    end_date = '2013-10-20' # date |  (optional)
    page = 1 # int |  (optional) (default to 1)
    start_date = '2013-10-20' # date |  (optional)

    try:
        # Changes
        api_response = api_instance.person_changes(person_id, end_date=end_date, page=page, start_date=start_date)
        print("The response of DefaultApi->person_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->person_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **int**|  | 
 **end_date** | **date**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **start_date** | **date**|  | [optional] 

### Return type

[**PersonChanges200Response**](PersonChanges200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **person_combined_credits**
> PersonCombinedCredits200Response person_combined_credits(person_id, language=language)

Combined Credits

Get the combined movie and TV credits that belong to a person.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.person_combined_credits200_response import PersonCombinedCredits200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    person_id = 'person_id_example' # str | 
    language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Combined Credits
        api_response = api_instance.person_combined_credits(person_id, language=language)
        print("The response of DefaultApi->person_combined_credits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->person_combined_credits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **str**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**PersonCombinedCredits200Response**](PersonCombinedCredits200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **person_details**
> PersonDetails200Response person_details(person_id, append_to_response=append_to_response, language=language)

Details

Query the top level details of a person.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.person_details200_response import PersonDetails200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    person_id = 56 # int | 
    append_to_response = 'append_to_response_example' # str | comma separated list of endpoints within this namespace, 20 items max (optional)
    language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Details
        api_response = api_instance.person_details(person_id, append_to_response=append_to_response, language=language)
        print("The response of DefaultApi->person_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->person_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **int**|  | 
 **append_to_response** | **str**| comma separated list of endpoints within this namespace, 20 items max | [optional] 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**PersonDetails200Response**](PersonDetails200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **person_external_ids**
> PersonExternalIds200Response person_external_ids(person_id)

External IDs

Get the external ID's that belong to a person.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.person_external_ids200_response import PersonExternalIds200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    person_id = 56 # int | 

    try:
        # External IDs
        api_response = api_instance.person_external_ids(person_id)
        print("The response of DefaultApi->person_external_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->person_external_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **int**|  | 

### Return type

[**PersonExternalIds200Response**](PersonExternalIds200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **person_images**
> PersonImages200Response person_images(person_id)

Images

Get the profile images that belong to a person.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.person_images200_response import PersonImages200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    person_id = 56 # int | 

    try:
        # Images
        api_response = api_instance.person_images(person_id)
        print("The response of DefaultApi->person_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->person_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **int**|  | 

### Return type

[**PersonImages200Response**](PersonImages200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **person_latest_id**
> PersonLatestId200Response person_latest_id()

Latest

Get the newest created person. This is a live response and will continuously change.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.person_latest_id200_response import PersonLatestId200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Latest
        api_response = api_instance.person_latest_id()
        print("The response of DefaultApi->person_latest_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->person_latest_id: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PersonLatestId200Response**](PersonLatestId200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **person_movie_credits**
> PersonMovieCredits200Response person_movie_credits(person_id, language=language)

Movie Credits

Get the movie credits for a person.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.person_movie_credits200_response import PersonMovieCredits200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    person_id = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Movie Credits
        api_response = api_instance.person_movie_credits(person_id, language=language)
        print("The response of DefaultApi->person_movie_credits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->person_movie_credits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**PersonMovieCredits200Response**](PersonMovieCredits200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **person_popular_list**
> PersonPopularList200Response person_popular_list(language=language, page=page)

Popular

Get a list of people ordered by popularity.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.person_popular_list200_response import PersonPopularList200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)

    try:
        # Popular
        api_response = api_instance.person_popular_list(language=language, page=page)
        print("The response of DefaultApi->person_popular_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->person_popular_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]

### Return type

[**PersonPopularList200Response**](PersonPopularList200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **person_tagged_images**
> PersonTaggedImages200Response person_tagged_images(person_id, page=page)

Tagged Images

Get the tagged images for a person.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.person_tagged_images200_response import PersonTaggedImages200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    person_id = 56 # int | 
    page = 1 # int |  (optional) (default to 1)

    try:
        # Tagged Images
        api_response = api_instance.person_tagged_images(person_id, page=page)
        print("The response of DefaultApi->person_tagged_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->person_tagged_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **int**|  | 
 **page** | **int**|  | [optional] [default to 1]

### Return type

[**PersonTaggedImages200Response**](PersonTaggedImages200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **person_tv_credits**
> PersonTvCredits200Response person_tv_credits(person_id, language=language)

TV Credits

Get the TV credits that belong to a person.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.person_tv_credits200_response import PersonTvCredits200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    person_id = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # TV Credits
        api_response = api_instance.person_tv_credits(person_id, language=language)
        print("The response of DefaultApi->person_tv_credits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->person_tv_credits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**PersonTvCredits200Response**](PersonTvCredits200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **review_details**
> ReviewDetails200Response review_details(review_id)

Details

Retrieve the details of a movie or TV show review.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.review_details200_response import ReviewDetails200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    review_id = 'review_id_example' # str | 

    try:
        # Details
        api_response = api_instance.review_details(review_id)
        print("The response of DefaultApi->review_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->review_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review_id** | **str**|  | 

### Return type

[**ReviewDetails200Response**](ReviewDetails200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_collection**
> SearchCollection200Response search_collection(query, include_adult=include_adult, language=language, page=page, region=region)

Collection

Search for collections by their original, translated and alternative names.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.search_collection200_response import SearchCollection200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    query = 'query_example' # str | 
    include_adult = False # bool |  (optional) (default to False)
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)
    region = 'region_example' # str |  (optional)

    try:
        # Collection
        api_response = api_instance.search_collection(query, include_adult=include_adult, language=language, page=page, region=region)
        print("The response of DefaultApi->search_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->search_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **include_adult** | **bool**|  | [optional] [default to False]
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]
 **region** | **str**|  | [optional] 

### Return type

[**SearchCollection200Response**](SearchCollection200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_company**
> SearchCompany200Response search_company(query, page=page)

Company

Search for companies by their original and alternative names.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.search_company200_response import SearchCompany200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    query = 'query_example' # str | 
    page = 1 # int |  (optional) (default to 1)

    try:
        # Company
        api_response = api_instance.search_company(query, page=page)
        print("The response of DefaultApi->search_company:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->search_company: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]

### Return type

[**SearchCompany200Response**](SearchCompany200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_keyword**
> SearchKeyword200Response search_keyword(query, page=page)

Keyword

Search for keywords by their name.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.search_keyword200_response import SearchKeyword200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    query = 'query_example' # str | 
    page = 1 # int |  (optional) (default to 1)

    try:
        # Keyword
        api_response = api_instance.search_keyword(query, page=page)
        print("The response of DefaultApi->search_keyword:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->search_keyword: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]

### Return type

[**SearchKeyword200Response**](SearchKeyword200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_movie**
> SearchMovie200Response search_movie(query, include_adult=include_adult, language=language, primary_release_year=primary_release_year, page=page, region=region, year=year)

Movie

Search for movies by their original, translated and alternative titles.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.search_movie200_response import SearchMovie200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    query = 'query_example' # str | 
    include_adult = False # bool |  (optional) (default to False)
    language = 'en-US' # str |  (optional) (default to 'en-US')
    primary_release_year = 'primary_release_year_example' # str |  (optional)
    page = 1 # int |  (optional) (default to 1)
    region = 'region_example' # str |  (optional)
    year = 'year_example' # str |  (optional)

    try:
        # Movie
        api_response = api_instance.search_movie(query, include_adult=include_adult, language=language, primary_release_year=primary_release_year, page=page, region=region, year=year)
        print("The response of DefaultApi->search_movie:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->search_movie: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **include_adult** | **bool**|  | [optional] [default to False]
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **primary_release_year** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **region** | **str**|  | [optional] 
 **year** | **str**|  | [optional] 

### Return type

[**SearchMovie200Response**](SearchMovie200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_multi**
> SearchMulti200Response search_multi(query, include_adult=include_adult, language=language, page=page)

Multi

Use multi search when you want to search for movies, TV shows and people in a single request.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.search_multi200_response import SearchMulti200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    query = 'query_example' # str | 
    include_adult = False # bool |  (optional) (default to False)
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)

    try:
        # Multi
        api_response = api_instance.search_multi(query, include_adult=include_adult, language=language, page=page)
        print("The response of DefaultApi->search_multi:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->search_multi: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **include_adult** | **bool**|  | [optional] [default to False]
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]

### Return type

[**SearchMulti200Response**](SearchMulti200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_person**
> SearchPerson200Response search_person(query, include_adult=include_adult, language=language, page=page)

Person

Search for people by their name and also known as names.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.search_person200_response import SearchPerson200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    query = 'query_example' # str | 
    include_adult = False # bool |  (optional) (default to False)
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)

    try:
        # Person
        api_response = api_instance.search_person(query, include_adult=include_adult, language=language, page=page)
        print("The response of DefaultApi->search_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->search_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **include_adult** | **bool**|  | [optional] [default to False]
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]

### Return type

[**SearchPerson200Response**](SearchPerson200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_tv**
> SearchTv200Response search_tv(query, first_air_date_year=first_air_date_year, include_adult=include_adult, language=language, page=page, year=year)

TV

Search for TV shows by their original, translated and also known as names.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.search_tv200_response import SearchTv200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    query = 'query_example' # str | 
    first_air_date_year = 56 # int | Search only the first air date. Valid values are: 1000..9999 (optional)
    include_adult = False # bool |  (optional) (default to False)
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)
    year = 56 # int | Search the first air date and all episode air dates. Valid values are: 1000..9999 (optional)

    try:
        # TV
        api_response = api_instance.search_tv(query, first_air_date_year=first_air_date_year, include_adult=include_adult, language=language, page=page, year=year)
        print("The response of DefaultApi->search_tv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->search_tv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **first_air_date_year** | **int**| Search only the first air date. Valid values are: 1000..9999 | [optional] 
 **include_adult** | **bool**|  | [optional] [default to False]
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]
 **year** | **int**| Search the first air date and all episode air dates. Valid values are: 1000..9999 | [optional] 

### Return type

[**SearchTv200Response**](SearchTv200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translations**
> Translations200Response translations(person_id)

Translations

Get the translations that belong to a person.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.translations200_response import Translations200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    person_id = 56 # int | 

    try:
        # Translations
        api_response = api_instance.translations(person_id)
        print("The response of DefaultApi->translations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->translations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **int**|  | 

### Return type

[**Translations200Response**](Translations200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trending_all**
> TrendingAll200Response trending_all(time_window, language=language)

All

Get the trending movies, TV shows and people.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.trending_all200_response import TrendingAll200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    time_window = 'day' # str |  (default to 'day')
    language = 'en-US' # str | `ISO-639-1`-`ISO-3166-1` code (optional) (default to 'en-US')

    try:
        # All
        api_response = api_instance.trending_all(time_window, language=language)
        print("The response of DefaultApi->trending_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->trending_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_window** | **str**|  | [default to &#39;day&#39;]
 **language** | **str**| &#x60;ISO-639-1&#x60;-&#x60;ISO-3166-1&#x60; code | [optional] [default to &#39;en-US&#39;]

### Return type

[**TrendingAll200Response**](TrendingAll200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trending_movies**
> TrendingAll200Response trending_movies(time_window, language=language)

Movies

Get the trending movies on TMDB.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.trending_all200_response import TrendingAll200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    time_window = 'day' # str |  (default to 'day')
    language = 'en-US' # str | `ISO-639-1`-`ISO-3166-1` code (optional) (default to 'en-US')

    try:
        # Movies
        api_response = api_instance.trending_movies(time_window, language=language)
        print("The response of DefaultApi->trending_movies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->trending_movies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_window** | **str**|  | [default to &#39;day&#39;]
 **language** | **str**| &#x60;ISO-639-1&#x60;-&#x60;ISO-3166-1&#x60; code | [optional] [default to &#39;en-US&#39;]

### Return type

[**TrendingAll200Response**](TrendingAll200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trending_people**
> TrendingPeople200Response trending_people(time_window, language=language)

People

Get the trending people on TMDB.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.trending_people200_response import TrendingPeople200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    time_window = 'day' # str |  (default to 'day')
    language = 'en-US' # str | `ISO-639-1`-`ISO-3166-1` code (optional) (default to 'en-US')

    try:
        # People
        api_response = api_instance.trending_people(time_window, language=language)
        print("The response of DefaultApi->trending_people:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->trending_people: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_window** | **str**|  | [default to &#39;day&#39;]
 **language** | **str**| &#x60;ISO-639-1&#x60;-&#x60;ISO-3166-1&#x60; code | [optional] [default to &#39;en-US&#39;]

### Return type

[**TrendingPeople200Response**](TrendingPeople200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trending_tv**
> TrendingTv200Response trending_tv(time_window, language=language)

TV

Get the trending TV shows on TMDB.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.trending_tv200_response import TrendingTv200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    time_window = 'day' # str |  (default to 'day')
    language = 'en-US' # str | `ISO-639-1`-`ISO-3166-1` code (optional) (default to 'en-US')

    try:
        # TV
        api_response = api_instance.trending_tv(time_window, language=language)
        print("The response of DefaultApi->trending_tv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->trending_tv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_window** | **str**|  | [default to &#39;day&#39;]
 **language** | **str**| &#x60;ISO-639-1&#x60;-&#x60;ISO-3166-1&#x60; code | [optional] [default to &#39;en-US&#39;]

### Return type

[**TrendingTv200Response**](TrendingTv200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_episode_account_states**
> MovieAccountStates200Response tv_episode_account_states(series_id, season_number, episode_number, session_id=session_id, guest_session_id=guest_session_id)

Account States

Get the rating, watchlist and favourite status.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_account_states200_response import MovieAccountStates200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    season_number = 56 # int | 
    episode_number = 56 # int | 
    session_id = 'session_id_example' # str |  (optional)
    guest_session_id = 'guest_session_id_example' # str |  (optional)

    try:
        # Account States
        api_response = api_instance.tv_episode_account_states(series_id, season_number, episode_number, session_id=session_id, guest_session_id=guest_session_id)
        print("The response of DefaultApi->tv_episode_account_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_episode_account_states: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **season_number** | **int**|  | 
 **episode_number** | **int**|  | 
 **session_id** | **str**|  | [optional] 
 **guest_session_id** | **str**|  | [optional] 

### Return type

[**MovieAccountStates200Response**](MovieAccountStates200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_episode_add_rating**
> MovieAddRating200Response tv_episode_add_rating(series_id, content_type, season_number, episode_number, guest_session_id=guest_session_id, session_id=session_id, movie_add_rating_request=movie_add_rating_request)

Add Rating

Rate a TV episode and save it to your rated list.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_add_rating200_response import MovieAddRating200Response
from openapi_client.models.movie_add_rating_request import MovieAddRatingRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    content_type = 'application/json;charset=utf-8' # str |  (default to 'application/json;charset=utf-8')
    season_number = 56 # int | 
    episode_number = 56 # int | 
    guest_session_id = 'guest_session_id_example' # str |  (optional)
    session_id = 'session_id_example' # str |  (optional)
    movie_add_rating_request = {value=8.5} # MovieAddRatingRequest |  (optional)

    try:
        # Add Rating
        api_response = api_instance.tv_episode_add_rating(series_id, content_type, season_number, episode_number, guest_session_id=guest_session_id, session_id=session_id, movie_add_rating_request=movie_add_rating_request)
        print("The response of DefaultApi->tv_episode_add_rating:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_episode_add_rating: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **content_type** | **str**|  | [default to &#39;application/json;charset&#x3D;utf-8&#39;]
 **season_number** | **int**|  | 
 **episode_number** | **int**|  | 
 **guest_session_id** | **str**|  | [optional] 
 **session_id** | **str**|  | [optional] 
 **movie_add_rating_request** | [**MovieAddRatingRequest**](MovieAddRatingRequest.md)|  | [optional] 

### Return type

[**MovieAddRating200Response**](MovieAddRating200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_episode_changes_by_id**
> TvEpisodeChangesById200Response tv_episode_changes_by_id(episode_id)

Changes

Get the recent changes for a TV episode.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_episode_changes_by_id200_response import TvEpisodeChangesById200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    episode_id = 56 # int | 

    try:
        # Changes
        api_response = api_instance.tv_episode_changes_by_id(episode_id)
        print("The response of DefaultApi->tv_episode_changes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_episode_changes_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **episode_id** | **int**|  | 

### Return type

[**TvEpisodeChangesById200Response**](TvEpisodeChangesById200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_episode_credits**
> TvEpisodeCredits200Response tv_episode_credits(series_id, season_number, episode_number, language=language)

Credits



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_episode_credits200_response import TvEpisodeCredits200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    season_number = 56 # int | 
    episode_number = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Credits
        api_response = api_instance.tv_episode_credits(series_id, season_number, episode_number, language=language)
        print("The response of DefaultApi->tv_episode_credits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_episode_credits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **season_number** | **int**|  | 
 **episode_number** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TvEpisodeCredits200Response**](TvEpisodeCredits200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_episode_delete_rating**
> MovieDeleteRating200Response tv_episode_delete_rating(series_id, season_number, episode_number, content_type=content_type, guest_session_id=guest_session_id, session_id=session_id)

Delete Rating

Delete your rating on a TV episode.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_delete_rating200_response import MovieDeleteRating200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    season_number = 56 # int | 
    episode_number = 56 # int | 
    content_type = 'application/json;charset=utf-8' # str |  (optional) (default to 'application/json;charset=utf-8')
    guest_session_id = 'guest_session_id_example' # str |  (optional)
    session_id = 'session_id_example' # str |  (optional)

    try:
        # Delete Rating
        api_response = api_instance.tv_episode_delete_rating(series_id, season_number, episode_number, content_type=content_type, guest_session_id=guest_session_id, session_id=session_id)
        print("The response of DefaultApi->tv_episode_delete_rating:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_episode_delete_rating: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **season_number** | **int**|  | 
 **episode_number** | **int**|  | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json;charset&#x3D;utf-8&#39;]
 **guest_session_id** | **str**|  | [optional] 
 **session_id** | **str**|  | [optional] 

### Return type

[**MovieDeleteRating200Response**](MovieDeleteRating200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_episode_details**
> TvEpisodeDetails200Response tv_episode_details(series_id, season_number, episode_number, append_to_response=append_to_response, language=language)

Details

Query the details of a TV episode.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_episode_details200_response import TvEpisodeDetails200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    season_number = 56 # int | 
    episode_number = 56 # int | 
    append_to_response = 'append_to_response_example' # str | comma separated list of endpoints within this namespace, 20 items max (optional)
    language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Details
        api_response = api_instance.tv_episode_details(series_id, season_number, episode_number, append_to_response=append_to_response, language=language)
        print("The response of DefaultApi->tv_episode_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_episode_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **season_number** | **int**|  | 
 **episode_number** | **int**|  | 
 **append_to_response** | **str**| comma separated list of endpoints within this namespace, 20 items max | [optional] 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TvEpisodeDetails200Response**](TvEpisodeDetails200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_episode_external_ids**
> TvEpisodeExternalIds200Response tv_episode_external_ids(series_id, season_number, episode_number)

External IDs

Get a list of external IDs that have been added to a TV episode.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_episode_external_ids200_response import TvEpisodeExternalIds200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    season_number = 56 # int | 
    episode_number = 'episode_number_example' # str | 

    try:
        # External IDs
        api_response = api_instance.tv_episode_external_ids(series_id, season_number, episode_number)
        print("The response of DefaultApi->tv_episode_external_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_episode_external_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **season_number** | **int**|  | 
 **episode_number** | **str**|  | 

### Return type

[**TvEpisodeExternalIds200Response**](TvEpisodeExternalIds200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_episode_group_details**
> TvEpisodeGroupDetails200Response tv_episode_group_details(tv_episode_group_id)

Details

Get the details of a TV episode group.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_episode_group_details200_response import TvEpisodeGroupDetails200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tv_episode_group_id = 'tv_episode_group_id_example' # str | 

    try:
        # Details
        api_response = api_instance.tv_episode_group_details(tv_episode_group_id)
        print("The response of DefaultApi->tv_episode_group_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_episode_group_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tv_episode_group_id** | **str**|  | 

### Return type

[**TvEpisodeGroupDetails200Response**](TvEpisodeGroupDetails200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_episode_images**
> TvEpisodeImages200Response tv_episode_images(series_id, season_number, episode_number, include_image_language=include_image_language, language=language)

Images

Get the images that belong to a TV episode.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_episode_images200_response import TvEpisodeImages200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    season_number = 56 # int | 
    episode_number = 56 # int | 
    include_image_language = 'include_image_language_example' # str | specify a comma separated list of ISO-639-1 values to query, for example: `en,null` (optional)
    language = 'language_example' # str |  (optional)

    try:
        # Images
        api_response = api_instance.tv_episode_images(series_id, season_number, episode_number, include_image_language=include_image_language, language=language)
        print("The response of DefaultApi->tv_episode_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_episode_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **season_number** | **int**|  | 
 **episode_number** | **int**|  | 
 **include_image_language** | **str**| specify a comma separated list of ISO-639-1 values to query, for example: &#x60;en,null&#x60; | [optional] 
 **language** | **str**|  | [optional] 

### Return type

[**TvEpisodeImages200Response**](TvEpisodeImages200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_episode_translations**
> TvEpisodeTranslations200Response tv_episode_translations(series_id, season_number, episode_number)

Translations

Get the translations that have been added to a TV episode.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_episode_translations200_response import TvEpisodeTranslations200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    season_number = 56 # int | 
    episode_number = 56 # int | 

    try:
        # Translations
        api_response = api_instance.tv_episode_translations(series_id, season_number, episode_number)
        print("The response of DefaultApi->tv_episode_translations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_episode_translations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **season_number** | **int**|  | 
 **episode_number** | **int**|  | 

### Return type

[**TvEpisodeTranslations200Response**](TvEpisodeTranslations200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_episode_videos**
> TvSeasonVideos200Response tv_episode_videos(series_id, season_number, episode_number, include_video_language=include_video_language, language=language)

Videos

Get the videos that belong to a TV episode.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_season_videos200_response import TvSeasonVideos200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    season_number = 56 # int | 
    episode_number = 56 # int | 
    include_video_language = 'include_video_language_example' # str | filter the list results by language, supports more than one value by using a comma (optional)
    language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Videos
        api_response = api_instance.tv_episode_videos(series_id, season_number, episode_number, include_video_language=include_video_language, language=language)
        print("The response of DefaultApi->tv_episode_videos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_episode_videos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **season_number** | **int**|  | 
 **episode_number** | **int**|  | 
 **include_video_language** | **str**| filter the list results by language, supports more than one value by using a comma | [optional] 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TvSeasonVideos200Response**](TvSeasonVideos200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_season_account_states**
> TvSeasonAccountStates200Response tv_season_account_states(series_id, season_number, session_id=session_id, guest_session_id=guest_session_id)

Account States

Get the rating, watchlist and favourite status.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_season_account_states200_response import TvSeasonAccountStates200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    season_number = 56 # int | 
    session_id = 'session_id_example' # str |  (optional)
    guest_session_id = 'guest_session_id_example' # str |  (optional)

    try:
        # Account States
        api_response = api_instance.tv_season_account_states(series_id, season_number, session_id=session_id, guest_session_id=guest_session_id)
        print("The response of DefaultApi->tv_season_account_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_season_account_states: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **season_number** | **int**|  | 
 **session_id** | **str**|  | [optional] 
 **guest_session_id** | **str**|  | [optional] 

### Return type

[**TvSeasonAccountStates200Response**](TvSeasonAccountStates200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_season_aggregate_credits**
> TvSeasonAggregateCredits200Response tv_season_aggregate_credits(series_id, season_number, language=language)

Aggregate Credits

Get the aggregate credits (cast and crew) that have been added to a TV season.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_season_aggregate_credits200_response import TvSeasonAggregateCredits200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    season_number = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Aggregate Credits
        api_response = api_instance.tv_season_aggregate_credits(series_id, season_number, language=language)
        print("The response of DefaultApi->tv_season_aggregate_credits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_season_aggregate_credits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **season_number** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TvSeasonAggregateCredits200Response**](TvSeasonAggregateCredits200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_season_changes_by_id**
> TvSeasonChangesById200Response tv_season_changes_by_id(season_id, end_date=end_date, page=page, start_date=start_date)

Changes

Get the recent changes for a TV season.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_season_changes_by_id200_response import TvSeasonChangesById200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    season_id = 56 # int | 
    end_date = 'end_date_example' # str |  (optional)
    page = 1 # int |  (optional) (default to 1)
    start_date = 'start_date_example' # str |  (optional)

    try:
        # Changes
        api_response = api_instance.tv_season_changes_by_id(season_id, end_date=end_date, page=page, start_date=start_date)
        print("The response of DefaultApi->tv_season_changes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_season_changes_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season_id** | **int**|  | 
 **end_date** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **start_date** | **str**|  | [optional] 

### Return type

[**TvSeasonChangesById200Response**](TvSeasonChangesById200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_season_credits**
> TvSeasonCredits200Response tv_season_credits(series_id, season_number, language=language)

Credits



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_season_credits200_response import TvSeasonCredits200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    season_number = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Credits
        api_response = api_instance.tv_season_credits(series_id, season_number, language=language)
        print("The response of DefaultApi->tv_season_credits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_season_credits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **season_number** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TvSeasonCredits200Response**](TvSeasonCredits200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_season_details**
> TvSeasonDetails200Response tv_season_details(series_id, season_number, append_to_response=append_to_response, language=language)

Details

Query the details of a TV season.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_season_details200_response import TvSeasonDetails200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    season_number = 56 # int | 
    append_to_response = 'append_to_response_example' # str | comma separated list of endpoints within this namespace, 20 items max (optional)
    language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Details
        api_response = api_instance.tv_season_details(series_id, season_number, append_to_response=append_to_response, language=language)
        print("The response of DefaultApi->tv_season_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_season_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **season_number** | **int**|  | 
 **append_to_response** | **str**| comma separated list of endpoints within this namespace, 20 items max | [optional] 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TvSeasonDetails200Response**](TvSeasonDetails200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_season_external_ids**
> TvSeasonExternalIds200Response tv_season_external_ids(series_id, season_number)

External IDs

Get a list of external IDs that have been added to a TV season.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_season_external_ids200_response import TvSeasonExternalIds200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    season_number = 56 # int | 

    try:
        # External IDs
        api_response = api_instance.tv_season_external_ids(series_id, season_number)
        print("The response of DefaultApi->tv_season_external_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_season_external_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **season_number** | **int**|  | 

### Return type

[**TvSeasonExternalIds200Response**](TvSeasonExternalIds200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_season_images**
> TvSeasonImages200Response tv_season_images(series_id, season_number, include_image_language=include_image_language, language=language)

Images

Get the images that belong to a TV season.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_season_images200_response import TvSeasonImages200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    season_number = 56 # int | 
    include_image_language = 'include_image_language_example' # str | specify a comma separated list of ISO-639-1 values to query, for example: `en,null` (optional)
    language = 'language_example' # str |  (optional)

    try:
        # Images
        api_response = api_instance.tv_season_images(series_id, season_number, include_image_language=include_image_language, language=language)
        print("The response of DefaultApi->tv_season_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_season_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **season_number** | **int**|  | 
 **include_image_language** | **str**| specify a comma separated list of ISO-639-1 values to query, for example: &#x60;en,null&#x60; | [optional] 
 **language** | **str**|  | [optional] 

### Return type

[**TvSeasonImages200Response**](TvSeasonImages200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_season_translations**
> TvSeasonTranslations200Response tv_season_translations(series_id, season_number)

Translations

Get the translations for a TV season.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_season_translations200_response import TvSeasonTranslations200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    season_number = 56 # int | 

    try:
        # Translations
        api_response = api_instance.tv_season_translations(series_id, season_number)
        print("The response of DefaultApi->tv_season_translations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_season_translations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **season_number** | **int**|  | 

### Return type

[**TvSeasonTranslations200Response**](TvSeasonTranslations200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_season_videos**
> TvSeasonVideos200Response tv_season_videos(series_id, season_number, include_video_language=include_video_language, language=language)

Videos

Get the videos that belong to a TV season.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_season_videos200_response import TvSeasonVideos200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    season_number = 56 # int | 
    include_video_language = 'include_video_language_example' # str | filter the list results by language, supports more than one value by using a comma (optional)
    language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Videos
        api_response = api_instance.tv_season_videos(series_id, season_number, include_video_language=include_video_language, language=language)
        print("The response of DefaultApi->tv_season_videos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_season_videos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **season_number** | **int**|  | 
 **include_video_language** | **str**| filter the list results by language, supports more than one value by using a comma | [optional] 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TvSeasonVideos200Response**](TvSeasonVideos200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_season_watch_providers**
> TvSeasonWatchProviders200Response tv_season_watch_providers(series_id, season_number, language=language)

Watch Providers

Get the list of streaming providers we have for a TV season.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_season_watch_providers200_response import TvSeasonWatchProviders200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    season_number = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Watch Providers
        api_response = api_instance.tv_season_watch_providers(series_id, season_number, language=language)
        print("The response of DefaultApi->tv_season_watch_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_season_watch_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **season_number** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TvSeasonWatchProviders200Response**](TvSeasonWatchProviders200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_series_account_states**
> MovieAccountStates200Response tv_series_account_states(series_id, session_id=session_id, guest_session_id=guest_session_id)

Account States

Get the rating, watchlist and favourite status.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_account_states200_response import MovieAccountStates200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    session_id = 'session_id_example' # str |  (optional)
    guest_session_id = 'guest_session_id_example' # str |  (optional)

    try:
        # Account States
        api_response = api_instance.tv_series_account_states(series_id, session_id=session_id, guest_session_id=guest_session_id)
        print("The response of DefaultApi->tv_series_account_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_series_account_states: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **session_id** | **str**|  | [optional] 
 **guest_session_id** | **str**|  | [optional] 

### Return type

[**MovieAccountStates200Response**](MovieAccountStates200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_series_add_rating**
> MovieAddRating200Response tv_series_add_rating(series_id, content_type, guest_session_id=guest_session_id, session_id=session_id, movie_add_rating_request=movie_add_rating_request)

Add Rating

Rate a TV show and save it to your rated list.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_add_rating200_response import MovieAddRating200Response
from openapi_client.models.movie_add_rating_request import MovieAddRatingRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    content_type = 'application/json;charset=utf-8' # str |  (default to 'application/json;charset=utf-8')
    guest_session_id = 'guest_session_id_example' # str |  (optional)
    session_id = 'session_id_example' # str |  (optional)
    movie_add_rating_request = {value=8.5} # MovieAddRatingRequest |  (optional)

    try:
        # Add Rating
        api_response = api_instance.tv_series_add_rating(series_id, content_type, guest_session_id=guest_session_id, session_id=session_id, movie_add_rating_request=movie_add_rating_request)
        print("The response of DefaultApi->tv_series_add_rating:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_series_add_rating: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **content_type** | **str**|  | [default to &#39;application/json;charset&#x3D;utf-8&#39;]
 **guest_session_id** | **str**|  | [optional] 
 **session_id** | **str**|  | [optional] 
 **movie_add_rating_request** | [**MovieAddRatingRequest**](MovieAddRatingRequest.md)|  | [optional] 

### Return type

[**MovieAddRating200Response**](MovieAddRating200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_series_aggregate_credits**
> TvSeriesAggregateCredits200Response tv_series_aggregate_credits(series_id, language=language)

Aggregate Credits

Get the aggregate credits (cast and crew) that have been added to a TV show.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_series_aggregate_credits200_response import TvSeriesAggregateCredits200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Aggregate Credits
        api_response = api_instance.tv_series_aggregate_credits(series_id, language=language)
        print("The response of DefaultApi->tv_series_aggregate_credits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_series_aggregate_credits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TvSeriesAggregateCredits200Response**](TvSeriesAggregateCredits200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_series_airing_today_list**
> TvSeriesAiringTodayList200Response tv_series_airing_today_list(language=language, page=page, timezone=timezone)

Airing Today

Get a list of TV shows airing today.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_series_airing_today_list200_response import TvSeriesAiringTodayList200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)
    timezone = 'timezone_example' # str |  (optional)

    try:
        # Airing Today
        api_response = api_instance.tv_series_airing_today_list(language=language, page=page, timezone=timezone)
        print("The response of DefaultApi->tv_series_airing_today_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_series_airing_today_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]
 **timezone** | **str**|  | [optional] 

### Return type

[**TvSeriesAiringTodayList200Response**](TvSeriesAiringTodayList200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_series_alternative_titles**
> TvSeriesAlternativeTitles200Response tv_series_alternative_titles(series_id)

Alternative Titles

Get the alternative titles that have been added to a TV show.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_series_alternative_titles200_response import TvSeriesAlternativeTitles200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 

    try:
        # Alternative Titles
        api_response = api_instance.tv_series_alternative_titles(series_id)
        print("The response of DefaultApi->tv_series_alternative_titles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_series_alternative_titles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 

### Return type

[**TvSeriesAlternativeTitles200Response**](TvSeriesAlternativeTitles200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_series_changes**
> TvSeriesChanges200Response tv_series_changes(series_id, end_date=end_date, page=page, start_date=start_date)

Changes

Get the recent changes for a TV show.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_series_changes200_response import TvSeriesChanges200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    end_date = 'end_date_example' # str |  (optional)
    page = 1 # int |  (optional) (default to 1)
    start_date = 'start_date_example' # str |  (optional)

    try:
        # Changes
        api_response = api_instance.tv_series_changes(series_id, end_date=end_date, page=page, start_date=start_date)
        print("The response of DefaultApi->tv_series_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_series_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **end_date** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **start_date** | **str**|  | [optional] 

### Return type

[**TvSeriesChanges200Response**](TvSeriesChanges200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_series_content_ratings**
> TvSeriesContentRatings200Response tv_series_content_ratings(series_id)

Content Ratings

Get the content ratings that have been added to a TV show.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_series_content_ratings200_response import TvSeriesContentRatings200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 

    try:
        # Content Ratings
        api_response = api_instance.tv_series_content_ratings(series_id)
        print("The response of DefaultApi->tv_series_content_ratings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_series_content_ratings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 

### Return type

[**TvSeriesContentRatings200Response**](TvSeriesContentRatings200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_series_credits**
> TvSeriesCredits200Response tv_series_credits(series_id, language=language)

Credits

Get the latest season credits of a TV show.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_series_credits200_response import TvSeriesCredits200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Credits
        api_response = api_instance.tv_series_credits(series_id, language=language)
        print("The response of DefaultApi->tv_series_credits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_series_credits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TvSeriesCredits200Response**](TvSeriesCredits200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_series_delete_rating**
> MovieDeleteRating200Response tv_series_delete_rating(series_id, content_type=content_type, guest_session_id=guest_session_id, session_id=session_id)

Delete Rating



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_delete_rating200_response import MovieDeleteRating200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    content_type = 'application/json;charset=utf-8' # str |  (optional) (default to 'application/json;charset=utf-8')
    guest_session_id = 'guest_session_id_example' # str |  (optional)
    session_id = 'session_id_example' # str |  (optional)

    try:
        # Delete Rating
        api_response = api_instance.tv_series_delete_rating(series_id, content_type=content_type, guest_session_id=guest_session_id, session_id=session_id)
        print("The response of DefaultApi->tv_series_delete_rating:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_series_delete_rating: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json;charset&#x3D;utf-8&#39;]
 **guest_session_id** | **str**|  | [optional] 
 **session_id** | **str**|  | [optional] 

### Return type

[**MovieDeleteRating200Response**](MovieDeleteRating200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_series_details**
> TvSeriesDetails200Response tv_series_details(series_id, append_to_response=append_to_response, language=language)

Details

Get the details of a TV show.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_series_details200_response import TvSeriesDetails200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    append_to_response = 'append_to_response_example' # str | comma separated list of endpoints within this namespace, 20 items max (optional)
    language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Details
        api_response = api_instance.tv_series_details(series_id, append_to_response=append_to_response, language=language)
        print("The response of DefaultApi->tv_series_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_series_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **append_to_response** | **str**| comma separated list of endpoints within this namespace, 20 items max | [optional] 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TvSeriesDetails200Response**](TvSeriesDetails200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_series_episode_groups**
> TvSeriesEpisodeGroups200Response tv_series_episode_groups(series_id)

Episode Groups

Get the episode groups that have been added to a TV show.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_series_episode_groups200_response import TvSeriesEpisodeGroups200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 

    try:
        # Episode Groups
        api_response = api_instance.tv_series_episode_groups(series_id)
        print("The response of DefaultApi->tv_series_episode_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_series_episode_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 

### Return type

[**TvSeriesEpisodeGroups200Response**](TvSeriesEpisodeGroups200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_series_external_ids**
> TvSeriesExternalIds200Response tv_series_external_ids(series_id)

External IDs

Get a list of external IDs that have been added to a TV show.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_series_external_ids200_response import TvSeriesExternalIds200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 

    try:
        # External IDs
        api_response = api_instance.tv_series_external_ids(series_id)
        print("The response of DefaultApi->tv_series_external_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_series_external_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 

### Return type

[**TvSeriesExternalIds200Response**](TvSeriesExternalIds200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_series_images**
> MovieImages200Response tv_series_images(series_id, include_image_language=include_image_language, language=language)

Images

Get the images that belong to a TV series.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.movie_images200_response import MovieImages200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    include_image_language = 'include_image_language_example' # str | specify a comma separated list of ISO-639-1 values to query, for example: `en,null` (optional)
    language = 'language_example' # str |  (optional)

    try:
        # Images
        api_response = api_instance.tv_series_images(series_id, include_image_language=include_image_language, language=language)
        print("The response of DefaultApi->tv_series_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_series_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **include_image_language** | **str**| specify a comma separated list of ISO-639-1 values to query, for example: &#x60;en,null&#x60; | [optional] 
 **language** | **str**|  | [optional] 

### Return type

[**MovieImages200Response**](MovieImages200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_series_keywords**
> TvSeriesKeywords200Response tv_series_keywords(series_id)

Keywords

Get a list of keywords that have been added to a TV show.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_series_keywords200_response import TvSeriesKeywords200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 

    try:
        # Keywords
        api_response = api_instance.tv_series_keywords(series_id)
        print("The response of DefaultApi->tv_series_keywords:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_series_keywords: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 

### Return type

[**TvSeriesKeywords200Response**](TvSeriesKeywords200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_series_latest_id**
> TvSeriesLatestId200Response tv_series_latest_id()

Latest

Get the newest TV show ID.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_series_latest_id200_response import TvSeriesLatestId200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Latest
        api_response = api_instance.tv_series_latest_id()
        print("The response of DefaultApi->tv_series_latest_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_series_latest_id: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TvSeriesLatestId200Response**](TvSeriesLatestId200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_series_on_the_air_list**
> TvSeriesOnTheAirList200Response tv_series_on_the_air_list(language=language, page=page, timezone=timezone)

On The Air

Get a list of TV shows that air in the next 7 days.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_series_on_the_air_list200_response import TvSeriesOnTheAirList200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)
    timezone = 'timezone_example' # str |  (optional)

    try:
        # On The Air
        api_response = api_instance.tv_series_on_the_air_list(language=language, page=page, timezone=timezone)
        print("The response of DefaultApi->tv_series_on_the_air_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_series_on_the_air_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]
 **timezone** | **str**|  | [optional] 

### Return type

[**TvSeriesOnTheAirList200Response**](TvSeriesOnTheAirList200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_series_popular_list**
> TvSeriesPopularList200Response tv_series_popular_list(language=language, page=page)

Popular

Get a list of TV shows ordered by popularity.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_series_popular_list200_response import TvSeriesPopularList200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)

    try:
        # Popular
        api_response = api_instance.tv_series_popular_list(language=language, page=page)
        print("The response of DefaultApi->tv_series_popular_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_series_popular_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]

### Return type

[**TvSeriesPopularList200Response**](TvSeriesPopularList200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_series_recommendations**
> TvSeriesRecommendations200Response tv_series_recommendations(series_id, language=language, page=page)

Recommendations



### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_series_recommendations200_response import TvSeriesRecommendations200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)

    try:
        # Recommendations
        api_response = api_instance.tv_series_recommendations(series_id, language=language, page=page)
        print("The response of DefaultApi->tv_series_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_series_recommendations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]

### Return type

[**TvSeriesRecommendations200Response**](TvSeriesRecommendations200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_series_reviews**
> TvSeriesReviews200Response tv_series_reviews(series_id, language=language, page=page)

Reviews

Get the reviews that have been added to a TV show.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_series_reviews200_response import TvSeriesReviews200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)

    try:
        # Reviews
        api_response = api_instance.tv_series_reviews(series_id, language=language, page=page)
        print("The response of DefaultApi->tv_series_reviews:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_series_reviews: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]

### Return type

[**TvSeriesReviews200Response**](TvSeriesReviews200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_series_screened_theatrically**
> TvSeriesScreenedTheatrically200Response tv_series_screened_theatrically(series_id)

Screened Theatrically

Get the seasons and episodes that have screened theatrically.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_series_screened_theatrically200_response import TvSeriesScreenedTheatrically200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 

    try:
        # Screened Theatrically
        api_response = api_instance.tv_series_screened_theatrically(series_id)
        print("The response of DefaultApi->tv_series_screened_theatrically:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_series_screened_theatrically: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 

### Return type

[**TvSeriesScreenedTheatrically200Response**](TvSeriesScreenedTheatrically200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_series_similar**
> TvSeriesSimilar200Response tv_series_similar(series_id, language=language, page=page)

Similar

Get the similar TV shows.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_series_similar200_response import TvSeriesSimilar200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 'series_id_example' # str | 
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)

    try:
        # Similar
        api_response = api_instance.tv_series_similar(series_id, language=language, page=page)
        print("The response of DefaultApi->tv_series_similar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_series_similar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **str**|  | 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]

### Return type

[**TvSeriesSimilar200Response**](TvSeriesSimilar200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_series_top_rated_list**
> TvSeriesTopRatedList200Response tv_series_top_rated_list(language=language, page=page)

Top Rated

Get a list of TV shows ordered by rating.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_series_top_rated_list200_response import TvSeriesTopRatedList200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    language = 'en-US' # str |  (optional) (default to 'en-US')
    page = 1 # int |  (optional) (default to 1)

    try:
        # Top Rated
        api_response = api_instance.tv_series_top_rated_list(language=language, page=page)
        print("The response of DefaultApi->tv_series_top_rated_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_series_top_rated_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **page** | **int**|  | [optional] [default to 1]

### Return type

[**TvSeriesTopRatedList200Response**](TvSeriesTopRatedList200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_series_translations**
> TvSeriesTranslations200Response tv_series_translations(series_id)

Translations

Get the translations that have been added to a TV show.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_series_translations200_response import TvSeriesTranslations200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 

    try:
        # Translations
        api_response = api_instance.tv_series_translations(series_id)
        print("The response of DefaultApi->tv_series_translations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_series_translations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 

### Return type

[**TvSeriesTranslations200Response**](TvSeriesTranslations200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_series_videos**
> TvSeriesVideos200Response tv_series_videos(series_id, include_video_language=include_video_language, language=language)

Videos

Get the videos that belong to a TV show.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_series_videos200_response import TvSeriesVideos200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 
    include_video_language = 'include_video_language_example' # str | filter the list results by language, supports more than one value by using a comma (optional)
    language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Videos
        api_response = api_instance.tv_series_videos(series_id, include_video_language=include_video_language, language=language)
        print("The response of DefaultApi->tv_series_videos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_series_videos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 
 **include_video_language** | **str**| filter the list results by language, supports more than one value by using a comma | [optional] 
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TvSeriesVideos200Response**](TvSeriesVideos200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tv_series_watch_providers**
> TvSeriesWatchProviders200Response tv_series_watch_providers(series_id)

Watch Providers

Get the list of streaming providers we have for a TV show.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.tv_series_watch_providers200_response import TvSeriesWatchProviders200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    series_id = 56 # int | 

    try:
        # Watch Providers
        api_response = api_instance.tv_series_watch_providers(series_id)
        print("The response of DefaultApi->tv_series_watch_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tv_series_watch_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | 

### Return type

[**TvSeriesWatchProviders200Response**](TvSeriesWatchProviders200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_provider_tv_list**
> WatchProvidersMovieList200Response watch_provider_tv_list(language=language, watch_region=watch_region)

TV Providers

Get the list of streaming providers we have for TV shows.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.watch_providers_movie_list200_response import WatchProvidersMovieList200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    language = 'en-US' # str |  (optional) (default to 'en-US')
    watch_region = 'watch_region_example' # str |  (optional)

    try:
        # TV Providers
        api_response = api_instance.watch_provider_tv_list(language=language, watch_region=watch_region)
        print("The response of DefaultApi->watch_provider_tv_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->watch_provider_tv_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **watch_region** | **str**|  | [optional] 

### Return type

[**WatchProvidersMovieList200Response**](WatchProvidersMovieList200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_providers_available_regions**
> WatchProvidersAvailableRegions200Response watch_providers_available_regions(language=language)

Available Regions

Get the list of the countries we have watch provider (OTT/streaming) data for.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.watch_providers_available_regions200_response import WatchProvidersAvailableRegions200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        # Available Regions
        api_response = api_instance.watch_providers_available_regions(language=language)
        print("The response of DefaultApi->watch_providers_available_regions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->watch_providers_available_regions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**WatchProvidersAvailableRegions200Response**](WatchProvidersAvailableRegions200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_providers_movie_list**
> WatchProvidersMovieList200Response watch_providers_movie_list(language=language, watch_region=watch_region)

Movie Providers

Get the list of streaming providers we have for movies.

### Example

* Api Key Authentication (sec0):

```python
import openapi_client
from openapi_client.models.watch_providers_movie_list200_response import WatchProvidersMovieList200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.themoviedb.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themoviedb.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sec0
configuration.api_key['sec0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sec0'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    language = 'en-US' # str |  (optional) (default to 'en-US')
    watch_region = 'watch_region_example' # str |  (optional)

    try:
        # Movie Providers
        api_response = api_instance.watch_providers_movie_list(language=language, watch_region=watch_region)
        print("The response of DefaultApi->watch_providers_movie_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->watch_providers_movie_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | [optional] [default to &#39;en-US&#39;]
 **watch_region** | **str**|  | [optional] 

### Return type

[**WatchProvidersMovieList200Response**](WatchProvidersMovieList200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

