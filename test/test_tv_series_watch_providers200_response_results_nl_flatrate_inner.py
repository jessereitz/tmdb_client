# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_watch_providers200_response_results_nl_flatrate_inner import TvSeriesWatchProviders200ResponseResultsNLFlatrateInner

class TestTvSeriesWatchProviders200ResponseResultsNLFlatrateInner(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsNLFlatrateInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsNLFlatrateInner:
        """Test TvSeriesWatchProviders200ResponseResultsNLFlatrateInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsNLFlatrateInner`
        """
        model = TvSeriesWatchProviders200ResponseResultsNLFlatrateInner()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsNLFlatrateInner(
                logo_path = '/Ajqyt5aNxNGjmF9uOfxArGrdf3X.jpg',
                provider_id = 384,
                provider_name = 'HBO Max',
                display_priority = 47
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsNLFlatrateInner(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsNLFlatrateInner(self):
        """Test TvSeriesWatchProviders200ResponseResultsNLFlatrateInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()