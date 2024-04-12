# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_episode_group_details200_response_groups_inner_episodes_inner import TvEpisodeGroupDetails200ResponseGroupsInnerEpisodesInner

class TestTvEpisodeGroupDetails200ResponseGroupsInnerEpisodesInner(unittest.TestCase):
    """TvEpisodeGroupDetails200ResponseGroupsInnerEpisodesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvEpisodeGroupDetails200ResponseGroupsInnerEpisodesInner:
        """Test TvEpisodeGroupDetails200ResponseGroupsInnerEpisodesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvEpisodeGroupDetails200ResponseGroupsInnerEpisodesInner`
        """
        model = TvEpisodeGroupDetails200ResponseGroupsInnerEpisodesInner()
        if include_optional:
            return TvEpisodeGroupDetails200ResponseGroupsInnerEpisodesInner(
                air_date = '2015-06-17',
                episode_number = 3,
                id = 1078262,
                name = 'Jim Carrey: We Love Breathing What You're Burning, Baby',
                overview = 'Jerry’s full of testosterone as he steps into a ‘76 Lamborghini Countach with Jim Carrey, who’s between a three-week cleanse and a five-day silent retreat. After coffee, it’s off to Carrey’s studio to study a portrait of a gorilla with a machine gun. Wow.',
                production_code = '',
                runtime = None,
                season_number = 6,
                show_id = 59717,
                still_path = '/aOyE420zuFq9zWtEWjIccAiTrzU.jpg',
                vote_average = 7.4,
                vote_count = 5,
                order = 0
            )
        else:
            return TvEpisodeGroupDetails200ResponseGroupsInnerEpisodesInner(
        )
        """

    def testTvEpisodeGroupDetails200ResponseGroupsInnerEpisodesInner(self):
        """Test TvEpisodeGroupDetails200ResponseGroupsInnerEpisodesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
