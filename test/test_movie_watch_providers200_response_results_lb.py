# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_watch_providers200_response_results_lb import MovieWatchProviders200ResponseResultsLB

class TestMovieWatchProviders200ResponseResultsLB(unittest.TestCase):
    """MovieWatchProviders200ResponseResultsLB unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieWatchProviders200ResponseResultsLB:
        """Test MovieWatchProviders200ResponseResultsLB
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieWatchProviders200ResponseResultsLB`
        """
        model = MovieWatchProviders200ResponseResultsLB()
        if include_optional:
            return MovieWatchProviders200ResponseResultsLB(
                link = 'https://www.themoviedb.org/movie/550-fight-club/watch?locale=LB',
                flatrate = [
                    tmdb_client.models.movie_watch_providers_200_response_results_au_flatrate_inner.movie_watch_providers_200_response_results_AU_flatrate_inner(
                        logo_path = '/emthp39XA2YScoYL1p0sdbAH2WA.jpg', 
                        provider_id = 119, 
                        provider_name = 'Amazon Prime Video', 
                        display_priority = 1, )
                    ],
                buy = [
                    tmdb_client.models.movie_watch_providers_200_response_results_bh_buy_inner.movie_watch_providers_200_response_results_BH_buy_inner(
                        logo_path = '/tbEdFQDwx5LEVr8WpSeXQSIirVq.jpg', 
                        provider_id = 3, 
                        provider_name = 'Google Play Movies', 
                        display_priority = 1000, )
                    ]
            )
        else:
            return MovieWatchProviders200ResponseResultsLB(
        )
        """

    def testMovieWatchProviders200ResponseResultsLB(self):
        """Test MovieWatchProviders200ResponseResultsLB"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
