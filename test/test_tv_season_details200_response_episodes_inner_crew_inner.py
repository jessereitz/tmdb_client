# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_season_details200_response_episodes_inner_crew_inner import TvSeasonDetails200ResponseEpisodesInnerCrewInner

class TestTvSeasonDetails200ResponseEpisodesInnerCrewInner(unittest.TestCase):
    """TvSeasonDetails200ResponseEpisodesInnerCrewInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeasonDetails200ResponseEpisodesInnerCrewInner:
        """Test TvSeasonDetails200ResponseEpisodesInnerCrewInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeasonDetails200ResponseEpisodesInnerCrewInner`
        """
        model = TvSeasonDetails200ResponseEpisodesInnerCrewInner()
        if include_optional:
            return TvSeasonDetails200ResponseEpisodesInnerCrewInner(
                department = 'Directing',
                job = 'Director',
                credit_id = '5256c8a219c2956ff6046e77',
                adult = False,
                gender = 2,
                id = 44797,
                known_for_department = 'Directing',
                name = 'Timothy Van Patten',
                original_name = 'Timothy Van Patten',
                popularity = 6.048,
                profile_path = '/MzSOFrd99HRdr6pkSRSctk3kBR.jpg'
            )
        else:
            return TvSeasonDetails200ResponseEpisodesInnerCrewInner(
        )
        """

    def testTvSeasonDetails200ResponseEpisodesInnerCrewInner(self):
        """Test TvSeasonDetails200ResponseEpisodesInnerCrewInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
