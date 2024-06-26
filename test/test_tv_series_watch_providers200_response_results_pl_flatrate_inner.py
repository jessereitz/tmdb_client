# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_watch_providers200_response_results_pl_flatrate_inner import TvSeriesWatchProviders200ResponseResultsPLFlatrateInner

class TestTvSeriesWatchProviders200ResponseResultsPLFlatrateInner(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsPLFlatrateInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsPLFlatrateInner:
        """Test TvSeriesWatchProviders200ResponseResultsPLFlatrateInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsPLFlatrateInner`
        """
        model = TvSeriesWatchProviders200ResponseResultsPLFlatrateInner()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsPLFlatrateInner(
                logo_path = '/l5Wxbsgral716BOtZsGyPVNn8GC.jpg',
                provider_id = 250,
                provider_name = 'Horizon',
                display_priority = 7
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsPLFlatrateInner(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsPLFlatrateInner(self):
        """Test TvSeriesWatchProviders200ResponseResultsPLFlatrateInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
