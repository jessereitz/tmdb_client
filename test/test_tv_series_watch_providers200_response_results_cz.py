# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_watch_providers200_response_results_cz import TvSeriesWatchProviders200ResponseResultsCZ

class TestTvSeriesWatchProviders200ResponseResultsCZ(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsCZ unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsCZ:
        """Test TvSeriesWatchProviders200ResponseResultsCZ
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsCZ`
        """
        model = TvSeriesWatchProviders200ResponseResultsCZ()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsCZ(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=CZ',
                flatrate = [
                    openapi_client.models.tv_series_watch_providers_200_response_results_cz_flatrate_inner.tv_series_watch_providers_200_response_results_CZ_flatrate_inner(
                        logo_path = '/Ajqyt5aNxNGjmF9uOfxArGrdf3X.jpg', 
                        provider_id = 384, 
                        provider_name = 'HBO Max', 
                        display_priority = 22, )
                    ]
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsCZ(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsCZ(self):
        """Test TvSeriesWatchProviders200ResponseResultsCZ"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
