# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_watch_providers200_response_results_ie_buy_inner import TvSeriesWatchProviders200ResponseResultsIEBuyInner

class TestTvSeriesWatchProviders200ResponseResultsIEBuyInner(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsIEBuyInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsIEBuyInner:
        """Test TvSeriesWatchProviders200ResponseResultsIEBuyInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsIEBuyInner`
        """
        model = TvSeriesWatchProviders200ResponseResultsIEBuyInner()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsIEBuyInner(
                logo_path = '/2pCbao1J9s0DMak2KKnEzmzHni8.jpg',
                provider_id = 130,
                provider_name = 'Sky Store',
                display_priority = 9
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsIEBuyInner(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsIEBuyInner(self):
        """Test TvSeriesWatchProviders200ResponseResultsIEBuyInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
