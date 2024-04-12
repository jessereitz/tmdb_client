# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_watch_providers200_response_results_sn import TvSeriesWatchProviders200ResponseResultsSN

class TestTvSeriesWatchProviders200ResponseResultsSN(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsSN unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsSN:
        """Test TvSeriesWatchProviders200ResponseResultsSN
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsSN`
        """
        model = TvSeriesWatchProviders200ResponseResultsSN()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsSN(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=SN',
                flatrate = [
                    openapi_client.models.tv_series_watch_providers_200_response_results_gh_flatrate_inner.tv_series_watch_providers_200_response_results_GH_flatrate_inner(
                        logo_path = '/okiQZMXnqwv0aD3QDYmu5DBNLce.jpg', 
                        provider_id = 55, 
                        provider_name = 'ShowMax', 
                        display_priority = 11, )
                    ]
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsSN(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsSN(self):
        """Test TvSeriesWatchProviders200ResponseResultsSN"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
