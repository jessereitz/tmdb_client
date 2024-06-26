# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_season_watch_providers200_response_results_ug import TvSeasonWatchProviders200ResponseResultsUG

class TestTvSeasonWatchProviders200ResponseResultsUG(unittest.TestCase):
    """TvSeasonWatchProviders200ResponseResultsUG unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeasonWatchProviders200ResponseResultsUG:
        """Test TvSeasonWatchProviders200ResponseResultsUG
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeasonWatchProviders200ResponseResultsUG`
        """
        model = TvSeasonWatchProviders200ResponseResultsUG()
        if include_optional:
            return TvSeasonWatchProviders200ResponseResultsUG(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/season/1/watch?locale=UG',
                flatrate = [
                    tmdb_client.models.tv_series_watch_providers_200_response_results_ke_flatrate_inner.tv_series_watch_providers_200_response_results_KE_flatrate_inner(
                        logo_path = '/okiQZMXnqwv0aD3QDYmu5DBNLce.jpg', 
                        provider_id = 55, 
                        provider_name = 'ShowMax', 
                        display_priority = 10, )
                    ]
            )
        else:
            return TvSeasonWatchProviders200ResponseResultsUG(
        )
        """

    def testTvSeasonWatchProviders200ResponseResultsUG(self):
        """Test TvSeasonWatchProviders200ResponseResultsUG"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
