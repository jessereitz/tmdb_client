# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_season_watch_providers200_response_results_ec import TvSeasonWatchProviders200ResponseResultsEC

class TestTvSeasonWatchProviders200ResponseResultsEC(unittest.TestCase):
    """TvSeasonWatchProviders200ResponseResultsEC unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeasonWatchProviders200ResponseResultsEC:
        """Test TvSeasonWatchProviders200ResponseResultsEC
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeasonWatchProviders200ResponseResultsEC`
        """
        model = TvSeasonWatchProviders200ResponseResultsEC()
        if include_optional:
            return TvSeasonWatchProviders200ResponseResultsEC(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/season/1/watch?locale=EC',
                flatrate = [
                    tmdb_client.models.tv_series_watch_providers_200_response_results_ec_flatrate_inner.tv_series_watch_providers_200_response_results_EC_flatrate_inner(
                        logo_path = '/cDzkhgvozSr4GW2aRdV22uDuFpw.jpg', 
                        provider_id = 339, 
                        provider_name = 'Movistar Play', 
                        display_priority = 4, )
                    ]
            )
        else:
            return TvSeasonWatchProviders200ResponseResultsEC(
        )
        """

    def testTvSeasonWatchProviders200ResponseResultsEC(self):
        """Test TvSeasonWatchProviders200ResponseResultsEC"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
