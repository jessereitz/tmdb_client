# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_watch_providers200_response_results_sa_flatrate_inner import TvSeriesWatchProviders200ResponseResultsSAFlatrateInner

class TestTvSeriesWatchProviders200ResponseResultsSAFlatrateInner(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsSAFlatrateInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsSAFlatrateInner:
        """Test TvSeriesWatchProviders200ResponseResultsSAFlatrateInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsSAFlatrateInner`
        """
        model = TvSeriesWatchProviders200ResponseResultsSAFlatrateInner()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsSAFlatrateInner(
                logo_path = '/xEPXbwbfABzPrUTWbgtDFH1NOa.jpg',
                provider_id = 629,
                provider_name = 'OSN',
                display_priority = 25
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsSAFlatrateInner(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsSAFlatrateInner(self):
        """Test TvSeriesWatchProviders200ResponseResultsSAFlatrateInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
