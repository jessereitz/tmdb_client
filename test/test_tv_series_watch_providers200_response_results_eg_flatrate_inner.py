# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_watch_providers200_response_results_eg_flatrate_inner import TvSeriesWatchProviders200ResponseResultsEGFlatrateInner

class TestTvSeriesWatchProviders200ResponseResultsEGFlatrateInner(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsEGFlatrateInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsEGFlatrateInner:
        """Test TvSeriesWatchProviders200ResponseResultsEGFlatrateInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsEGFlatrateInner`
        """
        model = TvSeriesWatchProviders200ResponseResultsEGFlatrateInner()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsEGFlatrateInner(
                logo_path = '/xEPXbwbfABzPrUTWbgtDFH1NOa.jpg',
                provider_id = 629,
                provider_name = 'OSN',
                display_priority = 27
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsEGFlatrateInner(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsEGFlatrateInner(self):
        """Test TvSeriesWatchProviders200ResponseResultsEGFlatrateInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()