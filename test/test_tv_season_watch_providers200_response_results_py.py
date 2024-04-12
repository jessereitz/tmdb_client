# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_season_watch_providers200_response_results_py import TvSeasonWatchProviders200ResponseResultsPY

class TestTvSeasonWatchProviders200ResponseResultsPY(unittest.TestCase):
    """TvSeasonWatchProviders200ResponseResultsPY unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeasonWatchProviders200ResponseResultsPY:
        """Test TvSeasonWatchProviders200ResponseResultsPY
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeasonWatchProviders200ResponseResultsPY`
        """
        model = TvSeasonWatchProviders200ResponseResultsPY()
        if include_optional:
            return TvSeasonWatchProviders200ResponseResultsPY(
                link = 'https://www.themoviedb.org/tv/1399-game-of-thrones/season/1/watch?locale=PY',
                flatrate = [
                    openapi_client.models.tv_series_watch_providers_200_response_results_bo_flatrate_inner.tv_series_watch_providers_200_response_results_BO_flatrate_inner(
                        logo_path = '/Ajqyt5aNxNGjmF9uOfxArGrdf3X.jpg', 
                        provider_id = 384, 
                        provider_name = 'HBO Max', 
                        display_priority = 3, )
                    ]
            )
        else:
            return TvSeasonWatchProviders200ResponseResultsPY(
        )
        """

    def testTvSeasonWatchProviders200ResponseResultsPY(self):
        """Test TvSeasonWatchProviders200ResponseResultsPY"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()