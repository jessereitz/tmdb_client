# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_watch_providers200_response_results_ro_flatrate_inner import TvSeriesWatchProviders200ResponseResultsROFlatrateInner

class TestTvSeriesWatchProviders200ResponseResultsROFlatrateInner(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsROFlatrateInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsROFlatrateInner:
        """Test TvSeriesWatchProviders200ResponseResultsROFlatrateInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsROFlatrateInner`
        """
        model = TvSeriesWatchProviders200ResponseResultsROFlatrateInner()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsROFlatrateInner(
                logo_path = '/Ajqyt5aNxNGjmF9uOfxArGrdf3X.jpg',
                provider_id = 384,
                provider_name = 'HBO Max',
                display_priority = 17
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsROFlatrateInner(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsROFlatrateInner(self):
        """Test TvSeriesWatchProviders200ResponseResultsROFlatrateInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
