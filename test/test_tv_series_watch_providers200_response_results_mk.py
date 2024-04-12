# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_watch_providers200_response_results_mk import TvSeriesWatchProviders200ResponseResultsMK

class TestTvSeriesWatchProviders200ResponseResultsMK(unittest.TestCase):
    """TvSeriesWatchProviders200ResponseResultsMK unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesWatchProviders200ResponseResultsMK:
        """Test TvSeriesWatchProviders200ResponseResultsMK
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesWatchProviders200ResponseResultsMK`
        """
        model = TvSeriesWatchProviders200ResponseResultsMK()
        if include_optional:
            return TvSeriesWatchProviders200ResponseResultsMK(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/watch?locale=MK',
                flatrate = [
                    openapi_client.models.movie_watch_providers_200_response_results_mk_flatrate_inner.movie_watch_providers_200_response_results_MK_flatrate_inner(
                        logo_path = '/Ajqyt5aNxNGjmF9uOfxArGrdf3X.jpg', 
                        provider_id = 384, 
                        provider_name = 'HBO Max', 
                        display_priority = 29, )
                    ]
            )
        else:
            return TvSeriesWatchProviders200ResponseResultsMK(
        )
        """

    def testTvSeriesWatchProviders200ResponseResultsMK(self):
        """Test TvSeriesWatchProviders200ResponseResultsMK"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
