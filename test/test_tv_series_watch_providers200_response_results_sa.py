# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_watch_providers200_response_results_sa import TvSeriesWatchProviders200ResponseResultsSA

class TestTvSeriesWatchProviders200ResponseResultsSA(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsSA unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsSA:
        """Test TvSeriesWatchProviders200ResponseResultsSA
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsSA`
        """
        model = TvSeriesWatchProviders200ResponseResultsSA()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsSA(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=SA',
                flatrate = [
                    openapi_client.models.tv_series_watch_providers_200_response_results_sa_flatrate_inner.tv_series_watch_providers_200_response_results_SA_flatrate_inner(
                        logo_path = '/xEPXbwbfABzPrUTWbgtDFH1NOa.jpg', 
                        provider_id = 629, 
                        provider_name = 'OSN', 
                        display_priority = 25, )
                    ]
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsSA(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsSA(self):
        """Test TvSeriesWatchProviders200ResponseResultsSA"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()