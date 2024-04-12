# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_screened_theatrically200_response import TvSeriesScreenedTheatrically200Response

class TestTvSeriesScreenedTheatrically200Response(unittest.TestCase):
    """TvSeriesScreenedTheatrically200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesScreenedTheatrically200Response:
        """Test TvSeriesScreenedTheatrically200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesScreenedTheatrically200Response`
        """
        model = TvSeriesScreenedTheatrically200Response()
        if include_optional:
            return TvSeriesScreenedTheatrically200Response(
                id = 1399,
                results = [
                    tmdb_client.models.tv_series_screened_theatrically_200_response_results_inner.tv_series_screened_theatrically_200_response_results_inner(
                        id = 1159054, 
                        episode_number = 10, 
                        season_number = 5, )
                    ]
            )
        else:
            return TvSeriesScreenedTheatrically200Response(
        )
        """

    def testTvSeriesScreenedTheatrically200Response(self):
        """Test TvSeriesScreenedTheatrically200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
