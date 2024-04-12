# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_watch_providers200_response_results_al import MovieWatchProviders200ResponseResultsAL

class TestMovieWatchProviders200ResponseResultsAL(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsAL unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsAL:
        """Test MovieWatchProviders200ResponseResultsAL
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsAL`
        """
        model = MovieWatchProviders200ResponseResultsAL()
        if include_optional:
            return MovieWatchProviders200ResponseResultsAL(
                link = 'https://www.themoviedb.org/movie/550-fight-club/watch?locale=AL',
                buy = [
                    tmdb_client.models.movie_watch_providers_200_response_results_al_buy_inner.movie_watch_providers_200_response_results_AL_buy_inner(
                        logo_path = '/5GEbAhFW2S5T8zVc1MNvz00pIzM.jpg', 
                        provider_id = 35, 
                        provider_name = 'Rakuten TV', 
                        display_priority = 9, )
                    ]
            )
        else:
            return MovieWatchProviders200ResponseResultsAL(
        )
        """

    def testMovieWatchProviders200ResponseResultsAL(self):
        """Test MovieWatchProviders200ResponseResultsAL"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
