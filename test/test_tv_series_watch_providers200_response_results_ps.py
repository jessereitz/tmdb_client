# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_watch_providers200_response_results_ps import TvSeriesWatchProviders200ResponseResultsPS

class TestTvSeriesWatchProviders200ResponseResultsPS(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsPS unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsPS:
        """Test TvSeriesWatchProviders200ResponseResultsPS
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsPS`
        """
        model = TvSeriesWatchProviders200ResponseResultsPS()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsPS(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=PS',
                flatrate = [
                    openapi_client.models.tv_series_watch_providers_200_response_results_iq_flatrate_inner.tv_series_watch_providers_200_response_results_IQ_flatrate_inner(
                        logo_path = '/xEPXbwbfABzPrUTWbgtDFH1NOa.jpg', 
                        provider_id = 629, 
                        provider_name = 'OSN', 
                        display_priority = 12, )
                    ]
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsPS(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsPS(self):
        """Test TvSeriesWatchProviders200ResponseResultsPS"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
