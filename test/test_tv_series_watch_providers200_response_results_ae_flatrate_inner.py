# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_watch_providers200_response_results_ae_flatrate_inner import TvSeriesWatchProviders200ResponseResultsAEFlatrateInner

class TestTvSeriesWatchProviders200ResponseResultsAEFlatrateInner(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsAEFlatrateInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsAEFlatrateInner:
        """Test TvSeriesWatchProviders200ResponseResultsAEFlatrateInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsAEFlatrateInner`
        """
        model = TvSeriesWatchProviders200ResponseResultsAEFlatrateInner()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsAEFlatrateInner(
                logo_path = '/xEPXbwbfABzPrUTWbgtDFH1NOa.jpg',
                provider_id = 629,
                provider_name = 'OSN',
                display_priority = 11
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsAEFlatrateInner(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsAEFlatrateInner(self):
        """Test TvSeriesWatchProviders200ResponseResultsAEFlatrateInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
