# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_watch_providers200_response_results_ie_flatrate_inner import TvSeriesWatchProviders200ResponseResultsIEFlatrateInner

class TestTvSeriesWatchProviders200ResponseResultsIEFlatrateInner(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsIEFlatrateInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsIEFlatrateInner:
        """Test TvSeriesWatchProviders200ResponseResultsIEFlatrateInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsIEFlatrateInner`
        """
        model = TvSeriesWatchProviders200ResponseResultsIEFlatrateInner()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsIEFlatrateInner(
                logo_path = '/fBHHXKC34ffxAsQvDe0ZJbvmTEQ.jpg',
                provider_id = 29,
                provider_name = 'Sky Go',
                display_priority = 8
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsIEFlatrateInner(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsIEFlatrateInner(self):
        """Test TvSeriesWatchProviders200ResponseResultsIEFlatrateInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
