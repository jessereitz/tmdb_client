# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_details200_response_genres_inner import TvSeriesDetails200ResponseGenresInner

class TestTvSeriesDetails200ResponseGenresInner(unittest.TestCase):
    """TvSeriesDetails200ResponseGenresInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesDetails200ResponseGenresInner:
        """Test TvSeriesDetails200ResponseGenresInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesDetails200ResponseGenresInner`
        """
        model = TvSeriesDetails200ResponseGenresInner()
        if include_optional:
            return TvSeriesDetails200ResponseGenresInner(
                id = 10765,
                name = 'Sci-Fi & Fantasy'
            )
        else:
            return TvSeriesDetails200ResponseGenresInner(
        )
        """

    def testTvSeriesDetails200ResponseGenresInner(self):
        """Test TvSeriesDetails200ResponseGenresInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
