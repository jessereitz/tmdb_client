# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_watch_providers200_response_results_tt import TvSeriesWatchProviders200ResponseResultsTT

class TestTvSeriesWatchProviders200ResponseResultsTT(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsTT unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsTT:
        """Test TvSeriesWatchProviders200ResponseResultsTT
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsTT`
        """
        model = TvSeriesWatchProviders200ResponseResultsTT()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsTT(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=TT',
                flatrate = [
                    openapi_client.models.movie_watch_providers_200_response_results_tt_flatrate_inner.movie_watch_providers_200_response_results_TT_flatrate_inner(
                        logo_path = '/Ajqyt5aNxNGjmF9uOfxArGrdf3X.jpg', 
                        provider_id = 384, 
                        provider_name = 'HBO Max', 
                        display_priority = 11, )
                    ]
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsTT(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsTT(self):
        """Test TvSeriesWatchProviders200ResponseResultsTT"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
