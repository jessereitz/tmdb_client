# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_watch_providers200_response_results_de_flatrate_inner import TvSeriesWatchProviders200ResponseResultsDEFlatrateInner

class TestTvSeriesWatchProviders200ResponseResultsDEFlatrateInner(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsDEFlatrateInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsDEFlatrateInner:
        """Test TvSeriesWatchProviders200ResponseResultsDEFlatrateInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsDEFlatrateInner`
        """
        model = TvSeriesWatchProviders200ResponseResultsDEFlatrateInner()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsDEFlatrateInner(
                logo_path = '/MiVcYLkztM6qqLeVSYWHFCUcXx.jpg',
                provider_id = 30,
                provider_name = 'WOW',
                display_priority = 5
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsDEFlatrateInner(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsDEFlatrateInner(self):
        """Test TvSeriesWatchProviders200ResponseResultsDEFlatrateInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
