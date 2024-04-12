# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_watch_providers200_response_results_gh_flatrate_inner import TvSeriesWatchProviders200ResponseResultsGHFlatrateInner

class TestTvSeriesWatchProviders200ResponseResultsGHFlatrateInner(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsGHFlatrateInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsGHFlatrateInner:
        """Test TvSeriesWatchProviders200ResponseResultsGHFlatrateInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsGHFlatrateInner`
        """
        model = TvSeriesWatchProviders200ResponseResultsGHFlatrateInner()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsGHFlatrateInner(
                logo_path = '/okiQZMXnqwv0aD3QDYmu5DBNLce.jpg',
                provider_id = 55,
                provider_name = 'ShowMax',
                display_priority = 11
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsGHFlatrateInner(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsGHFlatrateInner(self):
        """Test TvSeriesWatchProviders200ResponseResultsGHFlatrateInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
