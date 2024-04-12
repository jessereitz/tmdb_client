# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_watch_providers200_response_results_au_flatrate_inner import TvSeriesWatchProviders200ResponseResultsAUFlatrateInner

class TestTvSeriesWatchProviders200ResponseResultsAUFlatrateInner(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsAUFlatrateInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsAUFlatrateInner:
        """Test TvSeriesWatchProviders200ResponseResultsAUFlatrateInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsAUFlatrateInner`
        """
        model = TvSeriesWatchProviders200ResponseResultsAUFlatrateInner()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsAUFlatrateInner(
                logo_path = '/d3ixI1no0EpTj2i7u0Sd2DBXVlG.jpg',
                provider_id = 385,
                provider_name = 'BINGE',
                display_priority = 3
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsAUFlatrateInner(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsAUFlatrateInner(self):
        """Test TvSeriesWatchProviders200ResponseResultsAUFlatrateInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
