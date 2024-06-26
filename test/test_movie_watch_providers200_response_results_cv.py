# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_watch_providers200_response_results_cv import MovieWatchProviders200ResponseResultsCV

class TestMovieWatchProviders200ResponseResultsCV(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsCV unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsCV:
        """Test MovieWatchProviders200ResponseResultsCV
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsCV`
        """
        model = MovieWatchProviders200ResponseResultsCV()
        if include_optional:
            return MovieWatchProviders200ResponseResultsCV(
                link = 'https://www.themoviedb.org/movie/550-fight-club/watch?locale=CV',
                buy = [
                    tmdb_client.models.movie_watch_providers_200_response_results_cv_buy_inner.movie_watch_providers_200_response_results_CV_buy_inner(
                        logo_path = '/peURlLlr8jggOwK53fJ5wdQl05y.jpg', 
                        provider_id = 2, 
                        provider_name = 'Apple TV', 
                        display_priority = 13, )
                    ],
                rent = [
                    tmdb_client.models.movie_watch_providers_200_response_results_cv_buy_inner.movie_watch_providers_200_response_results_CV_buy_inner(
                        logo_path = '/peURlLlr8jggOwK53fJ5wdQl05y.jpg', 
                        provider_id = 2, 
                        provider_name = 'Apple TV', 
                        display_priority = 13, )
                    ]
            )
        else:
            return MovieWatchProviders200ResponseResultsCV(
        )
        """

    def testMovieWatchProviders200ResponseResultsCV(self):
        """Test MovieWatchProviders200ResponseResultsCV"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
