# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_season_watch_providers200_response_results_rs import TvSeasonWatchProviders200ResponseResultsRS

class TestTvSeasonWatchProviders200ResponseResultsRS(unittest.TestCase):
    """TvSeasonWatchProviders200ResponseResultsRS unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeasonWatchProviders200ResponseResultsRS:
        """Test TvSeasonWatchProviders200ResponseResultsRS
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeasonWatchProviders200ResponseResultsRS`
        """
        model = TvSeasonWatchProviders200ResponseResultsRS()
        if include_optional:
            return TvSeasonWatchProviders200ResponseResultsRS(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/season/1/watch?locale=RS',
                flatrate = [
                    tmdb_client.models.tv_series_watch_providers_200_response_results_rs_flatrate_inner.tv_series_watch_providers_200_response_results_RS_flatrate_inner(
                        logo_path = '/Ajqyt5aNxNGjmF9uOfxArGrdf3X.jpg', 
                        provider_id = 384, 
                        provider_name = 'HBO Max', 
                        display_priority = 32, )
                    ]
            )
        else:
            return TvSeasonWatchProviders200ResponseResultsRS(
        )
        """

    def testTvSeasonWatchProviders200ResponseResultsRS(self):
        """Test TvSeasonWatchProviders200ResponseResultsRS"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
