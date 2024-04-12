# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_season_watch_providers200_response_results_iq import TvSeasonWatchProviders200ResponseResultsIQ

class TestTvSeasonWatchProviders200ResponseResultsIQ(unittest.TestCase):
    """TvSeasonWatchProviders200ResponseResultsIQ unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeasonWatchProviders200ResponseResultsIQ:
        """Test TvSeasonWatchProviders200ResponseResultsIQ
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeasonWatchProviders200ResponseResultsIQ`
        """
        model = TvSeasonWatchProviders200ResponseResultsIQ()
        if include_optional:
            return TvSeasonWatchProviders200ResponseResultsIQ(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/season/1/watch?locale=IQ',
                flatrate = [
                    openapi_client.models.tv_series_watch_providers_200_response_results_iq_flatrate_inner.tv_series_watch_providers_200_response_results_IQ_flatrate_inner(
                        logo_path = '/xEPXbwbfABzPrUTWbgtDFH1NOa.jpg', 
                        provider_id = 629, 
                        provider_name = 'OSN', 
                        display_priority = 12, )
                    ]
            )
        else:
            return TvSeasonWatchProviders200ResponseResultsIQ(
        )
        """

    def testTvSeasonWatchProviders200ResponseResultsIQ(self):
        """Test TvSeasonWatchProviders200ResponseResultsIQ"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()