# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_watch_providers200_response_results_ph_flatrate_inner import TvSeriesWatchProviders200ResponseResultsPHFlatrateInner

class TestTvSeriesWatchProviders200ResponseResultsPHFlatrateInner(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsPHFlatrateInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsPHFlatrateInner:
        """Test TvSeriesWatchProviders200ResponseResultsPHFlatrateInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsPHFlatrateInner`
        """
        model = TvSeriesWatchProviders200ResponseResultsPHFlatrateInner()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsPHFlatrateInner(
                logo_path = '/bxdNcDbk1ohVeOMmM3eusAAiTLw.jpg',
                provider_id = 425,
                provider_name = 'HBO Go',
                display_priority = 12
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsPHFlatrateInner(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsPHFlatrateInner(self):
        """Test TvSeriesWatchProviders200ResponseResultsPHFlatrateInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
