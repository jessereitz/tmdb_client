# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_details200_response_networks_inner import TvSeriesDetails200ResponseNetworksInner

class TestTvSeriesDetails200ResponseNetworksInner(unittest.TestCase):
    """TvSeriesDetails200ResponseNetworksInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesDetails200ResponseNetworksInner:
        """Test TvSeriesDetails200ResponseNetworksInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesDetails200ResponseNetworksInner`
        """
        model = TvSeriesDetails200ResponseNetworksInner()
        if include_optional:
            return TvSeriesDetails200ResponseNetworksInner(
                id = 49,
                logo_path = '/tuomPhY2UtuPTqqFnKMVHvSb724.png',
                name = 'HBO',
                origin_country = 'US'
            )
        else:
            return TvSeriesDetails200ResponseNetworksInner(
        )
        """

    def testTvSeriesDetails200ResponseNetworksInner(self):
        """Test TvSeriesDetails200ResponseNetworksInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
