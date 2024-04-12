# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_watch_providers200_response_results_nz import TvSeriesWatchProviders200ResponseResultsNZ

class TestTvSeriesWatchProviders200ResponseResultsNZ(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsNZ unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsNZ:
        """Test TvSeriesWatchProviders200ResponseResultsNZ
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsNZ`
        """
        model = TvSeriesWatchProviders200ResponseResultsNZ()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsNZ(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=NZ',
                flatrate = [
                    openapi_client.models.tv_series_watch_providers_200_response_results_nz_flatrate_inner.tv_series_watch_providers_200_response_results_NZ_flatrate_inner(
                        logo_path = '/od4YNSSLgOP3p8EtQTnEYfrPa77.jpg', 
                        provider_id = 273, 
                        provider_name = 'Neon TV', 
                        display_priority = 2, )
                    ]
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsNZ(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsNZ(self):
        """Test TvSeriesWatchProviders200ResponseResultsNZ"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
