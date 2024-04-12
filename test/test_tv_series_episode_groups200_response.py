# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_episode_groups200_response import TvSeriesEpisodeGroups200Response

class TestTvSeriesEpisodeGroups200Response(unittest.TestCase):
    """TvSeriesEpisodeGroups200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesEpisodeGroups200Response:
        """Test TvSeriesEpisodeGroups200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesEpisodeGroups200Response`
        """
        model = TvSeriesEpisodeGroups200Response()
        if include_optional:
            return TvSeriesEpisodeGroups200Response(
                results = [
                    tmdb_client.models.tv_series_episode_groups_200_response_results_inner.tv_series_episode_groups_200_response_results_inner(
                        description = '', 
                        episode_count = 102, 
                        group_count = 9, 
                        id = '5e9077d2e640d600151f32bd', 
                        name = 'Aired Order', 
                        network = tmdb_client.models.tv_series_details_200_response_networks_inner.tv_series_details_200_response_networks_inner(
                            id = 49, 
                            logo_path = '/tuomPhY2UtuPTqqFnKMVHvSb724.png', 
                            name = 'HBO', 
                            origin_country = 'US', ), 
                        type = 1, )
                    ],
                id = 1399
            )
        else:
            return TvSeriesEpisodeGroups200Response(
        )
        """

    def testTvSeriesEpisodeGroups200Response(self):
        """Test TvSeriesEpisodeGroups200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
