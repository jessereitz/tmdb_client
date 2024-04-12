# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_watch_providers200_response_results_ie import TvSeriesWatchProviders200ResponseResultsIE

class TestTvSeriesWatchProviders200ResponseResultsIE(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsIE unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsIE:
        """Test TvSeriesWatchProviders200ResponseResultsIE
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsIE`
        """
        model = TvSeriesWatchProviders200ResponseResultsIE()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsIE(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=IE',
                flatrate = [
                    openapi_client.models.tv_series_watch_providers_200_response_results_ie_flatrate_inner.tv_series_watch_providers_200_response_results_IE_flatrate_inner(
                        logo_path = '/fBHHXKC34ffxAsQvDe0ZJbvmTEQ.jpg', 
                        provider_id = 29, 
                        provider_name = 'Sky Go', 
                        display_priority = 8, )
                    ],
                buy = [
                    openapi_client.models.tv_series_watch_providers_200_response_results_ie_buy_inner.tv_series_watch_providers_200_response_results_IE_buy_inner(
                        logo_path = '/2pCbao1J9s0DMak2KKnEzmzHni8.jpg', 
                        provider_id = 130, 
                        provider_name = 'Sky Store', 
                        display_priority = 9, )
                    ]
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsIE(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsIE(self):
        """Test TvSeriesWatchProviders200ResponseResultsIE"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
