# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_watch_providers200_response_results_dk import MovieWatchProviders200ResponseResultsDK

class TestMovieWatchProviders200ResponseResultsDK(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsDK unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsDK:
        """Test MovieWatchProviders200ResponseResultsDK
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsDK`
        """
        model = MovieWatchProviders200ResponseResultsDK()
        if include_optional:
            return MovieWatchProviders200ResponseResultsDK(
                link = 'https://www.themoviedb.org/movie/550-fight-club/watch?locale=DK',
                rent = [
                    tmdb_client.models.movie_watch_providers_200_response_results_dk_rent_inner.movie_watch_providers_200_response_results_DK_rent_inner(
                        logo_path = '/peURlLlr8jggOwK53fJ5wdQl05y.jpg', 
                        provider_id = 2, 
                        provider_name = 'Apple TV', 
                        display_priority = 7, )
                    ],
                flatrate = [
                    tmdb_client.models.movie_watch_providers_200_response_results_be_flatrate_inner.movie_watch_providers_200_response_results_BE_flatrate_inner(
                        logo_path = '/7rwgEs15tFwyR9NPQ5vpzxTj19Q.jpg', 
                        provider_id = 337, 
                        provider_name = 'Disney Plus', 
                        display_priority = 1, )
                    ],
                buy = [
                    tmdb_client.models.movie_watch_providers_200_response_results_dk_rent_inner.movie_watch_providers_200_response_results_DK_rent_inner(
                        logo_path = '/peURlLlr8jggOwK53fJ5wdQl05y.jpg', 
                        provider_id = 2, 
                        provider_name = 'Apple TV', 
                        display_priority = 7, )
                    ]
            )
        else:
            return MovieWatchProviders200ResponseResultsDK(
        )
        """

    def testMovieWatchProviders200ResponseResultsDK(self):
        """Test MovieWatchProviders200ResponseResultsDK"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
