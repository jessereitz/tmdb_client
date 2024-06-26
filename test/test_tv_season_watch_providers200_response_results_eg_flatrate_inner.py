# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_season_watch_providers200_response_results_eg_flatrate_inner import TvSeasonWatchProviders200ResponseResultsEGFlatrateInner

class TestTvSeasonWatchProviders200ResponseResultsEGFlatrateInner(unittest.TestCase):
    """TvSeasonWatchProviders200ResponseResultsEGFlatrateInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeasonWatchProviders200ResponseResultsEGFlatrateInner:
        """Test TvSeasonWatchProviders200ResponseResultsEGFlatrateInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeasonWatchProviders200ResponseResultsEGFlatrateInner`
        """
        model = TvSeasonWatchProviders200ResponseResultsEGFlatrateInner()
        if include_optional:
            return TvSeasonWatchProviders200ResponseResultsEGFlatrateInner(
                logo_path = '/xEPXbwbfABzPrUTWbgtDFH1NOa.jpg',
                provider_id = 629,
                provider_name = 'OSN',
                display_priority = 28
            )
        else:
            return TvSeasonWatchProviders200ResponseResultsEGFlatrateInner(
        )
        """

    def testTvSeasonWatchProviders200ResponseResultsEGFlatrateInner(self):
        """Test TvSeasonWatchProviders200ResponseResultsEGFlatrateInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
