# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_season_watch_providers200_response_results_be import TvSeasonWatchProviders200ResponseResultsBE

class TestTvSeasonWatchProviders200ResponseResultsBE(unittest.TestCase):
    """TvSeasonWatchProviders200ResponseResultsBE unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeasonWatchProviders200ResponseResultsBE:
        """Test TvSeasonWatchProviders200ResponseResultsBE
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeasonWatchProviders200ResponseResultsBE`
        """
        model = TvSeasonWatchProviders200ResponseResultsBE()
        if include_optional:
            return TvSeasonWatchProviders200ResponseResultsBE(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/season/1/watch?locale=BE',
                flatrate = [
                    tmdb_client.models.tv_series_watch_providers_200_response_results_be_flatrate_inner.tv_series_watch_providers_200_response_results_BE_flatrate_inner(
                        logo_path = '/pq8p1umEnJjdFAP1nFvNArTR61X.jpg', 
                        provider_id = 311, 
                        provider_name = 'Be TV Go', 
                        display_priority = 4, )
                    ]
            )
        else:
            return TvSeasonWatchProviders200ResponseResultsBE(
        )
        """

    def testTvSeasonWatchProviders200ResponseResultsBE(self):
        """Test TvSeasonWatchProviders200ResponseResultsBE"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
