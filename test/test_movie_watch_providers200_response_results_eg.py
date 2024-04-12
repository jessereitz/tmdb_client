# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_watch_providers200_response_results_eg import MovieWatchProviders200ResponseResultsEG

class TestMovieWatchProviders200ResponseResultsEG(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsEG unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsEG:
        """Test MovieWatchProviders200ResponseResultsEG
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsEG`
        """
        model = MovieWatchProviders200ResponseResultsEG()
        if include_optional:
            return MovieWatchProviders200ResponseResultsEG(
                link = 'https://www.themoviedb.org/movie/550-fight-club/watch?locale=EG',
                rent = [
                    tmdb_client.models.movie_watch_providers_200_response_results_bg_rent_inner.movie_watch_providers_200_response_results_BG_rent_inner(
                        logo_path = '/peURlLlr8jggOwK53fJ5wdQl05y.jpg', 
                        provider_id = 2, 
                        provider_name = 'Apple TV', 
                        display_priority = 2, )
                    ],
                buy = [
                    tmdb_client.models.movie_watch_providers_200_response_results_bg_rent_inner.movie_watch_providers_200_response_results_BG_rent_inner(
                        logo_path = '/peURlLlr8jggOwK53fJ5wdQl05y.jpg', 
                        provider_id = 2, 
                        provider_name = 'Apple TV', 
                        display_priority = 2, )
                    ]
            )
        else:
            return MovieWatchProviders200ResponseResultsEG(
        )
        """

    def testMovieWatchProviders200ResponseResultsEG(self):
        """Test MovieWatchProviders200ResponseResultsEG"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
