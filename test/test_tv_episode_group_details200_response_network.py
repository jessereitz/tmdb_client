# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_episode_group_details200_response_network import TvEpisodeGroupDetails200ResponseNetwork

class TestTvEpisodeGroupDetails200ResponseNetwork(unittest.TestCase):
    """TvEpisodeGroupDetails200ResponseNetwork unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvEpisodeGroupDetails200ResponseNetwork:
        """Test TvEpisodeGroupDetails200ResponseNetwork
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvEpisodeGroupDetails200ResponseNetwork`
        """
        model = TvEpisodeGroupDetails200ResponseNetwork()
        if include_optional:
            return TvEpisodeGroupDetails200ResponseNetwork(
                id = 213,
                logo_path = '/wwemzKWzjKYJFfCeiB57q3r4Bcm.png',
                name = 'Netflix',
                origin_country = ''
            )
        else:
            return TvEpisodeGroupDetails200ResponseNetwork(
        )
        """

    def testTvEpisodeGroupDetails200ResponseNetwork(self):
        """Test TvEpisodeGroupDetails200ResponseNetwork"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
