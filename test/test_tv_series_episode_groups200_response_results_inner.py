# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_episode_groups200_response_results_inner import TvSeriesEpisodeGroups200ResponseResultsInner

class TestTvSeriesEpisodeGroups200ResponseResultsInner(unittest.TestCase):
    """TvSeriesEpisodeGroups200ResponseResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesEpisodeGroups200ResponseResultsInner:
        """Test TvSeriesEpisodeGroups200ResponseResultsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesEpisodeGroups200ResponseResultsInner`
        """
        model = TvSeriesEpisodeGroups200ResponseResultsInner()
        if include_optional:
            return TvSeriesEpisodeGroups200ResponseResultsInner(
                description = '',
                episode_count = 102,
                group_count = 9,
                id = '5e9077d2e640d600151f32bd',
                name = 'Aired Order',
                network = openapi_client.models.tv_series_details_200_response_networks_inner.tv_series_details_200_response_networks_inner(
                    id = 49, 
                    logo_path = '/tuomPhY2UtuPTqqFnKMVHvSb724.png', 
                    name = 'HBO', 
                    origin_country = 'US', ),
                type = 1
            )
        else:
            return TvSeriesEpisodeGroups200ResponseResultsInner(
        )
        """

    def testTvSeriesEpisodeGroups200ResponseResultsInner(self):
        """Test TvSeriesEpisodeGroups200ResponseResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
