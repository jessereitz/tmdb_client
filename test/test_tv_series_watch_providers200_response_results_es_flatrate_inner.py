# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_watch_providers200_response_results_es_flatrate_inner import TvSeriesWatchProviders200ResponseResultsESFlatrateInner

class TestTvSeriesWatchProviders200ResponseResultsESFlatrateInner(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsESFlatrateInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsESFlatrateInner:
        """Test TvSeriesWatchProviders200ResponseResultsESFlatrateInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsESFlatrateInner`
        """
        model = TvSeriesWatchProviders200ResponseResultsESFlatrateInner()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsESFlatrateInner(
                logo_path = '/Ajqyt5aNxNGjmF9uOfxArGrdf3X.jpg',
                provider_id = 384,
                provider_name = 'HBO Max',
                display_priority = 9
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsESFlatrateInner(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsESFlatrateInner(self):
        """Test TvSeriesWatchProviders200ResponseResultsESFlatrateInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()