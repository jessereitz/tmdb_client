# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_watch_providers200_response_results_pe import TvSeriesWatchProviders200ResponseResultsPE

class TestTvSeriesWatchProviders200ResponseResultsPE(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsPE unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsPE:
        """Test TvSeriesWatchProviders200ResponseResultsPE
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsPE`
        """
        model = TvSeriesWatchProviders200ResponseResultsPE()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsPE(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=PE',
                flatrate = [
                    openapi_client.models.tv_series_watch_providers_200_response_results_pe_flatrate_inner.tv_series_watch_providers_200_response_results_PE_flatrate_inner(
                        logo_path = '/Ajqyt5aNxNGjmF9uOfxArGrdf3X.jpg', 
                        provider_id = 384, 
                        provider_name = 'HBO Max', 
                        display_priority = 8, )
                    ]
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsPE(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsPE(self):
        """Test TvSeriesWatchProviders200ResponseResultsPE"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()