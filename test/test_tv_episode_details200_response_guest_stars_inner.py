# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_episode_details200_response_guest_stars_inner import TvEpisodeDetails200ResponseGuestStarsInner

class TestTvEpisodeDetails200ResponseGuestStarsInner(unittest.TestCase):
    """TvEpisodeDetails200ResponseGuestStarsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvEpisodeDetails200ResponseGuestStarsInner:
        """Test TvEpisodeDetails200ResponseGuestStarsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvEpisodeDetails200ResponseGuestStarsInner`
        """
        model = TvEpisodeDetails200ResponseGuestStarsInner()
        if include_optional:
            return TvEpisodeDetails200ResponseGuestStarsInner(
                character = 'Benjen Stark',
                credit_id = '5256c8b919c2956ff604836a',
                order = 62,
                adult = False,
                gender = 2,
                id = 119783,
                known_for_department = 'Acting',
                name = 'Joseph Mawle',
                original_name = 'Joseph Mawle',
                popularity = 6.758,
                profile_path = '/1Ocb9v3h54beGVoJMm4w50UQhLf.jpg'
            )
        else:
            return TvEpisodeDetails200ResponseGuestStarsInner(
        )
        """

    def testTvEpisodeDetails200ResponseGuestStarsInner(self):
        """Test TvEpisodeDetails200ResponseGuestStarsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
