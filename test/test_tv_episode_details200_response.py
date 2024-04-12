# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_episode_details200_response import TvEpisodeDetails200Response

class TestTvEpisodeDetails200Response(unittest.TestCase):
    """TvEpisodeDetails200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvEpisodeDetails200Response:
        """Test TvEpisodeDetails200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvEpisodeDetails200Response`
        """
        model = TvEpisodeDetails200Response()
        if include_optional:
            return TvEpisodeDetails200Response(
                air_date = '2011-04-17',
                crew = [
                    openapi_client.models.tv_episode_details_200_response_crew_inner.tv_episode_details_200_response_crew_inner(
                        department = 'Directing', 
                        job = 'Director', 
                        credit_id = '5256c8a219c2956ff6046e77', 
                        adult = False, 
                        gender = 2, 
                        id = 44797, 
                        known_for_department = 'Directing', 
                        name = 'Timothy Van Patten', 
                        original_name = 'Timothy Van Patten', 
                        popularity = 7.775, 
                        profile_path = '/MzSOFrd99HRdr6pkSRSctk3kBR.jpg', )
                    ],
                episode_number = 1,
                guest_stars = [
                    openapi_client.models.tv_episode_details_200_response_guest_stars_inner.tv_episode_details_200_response_guest_stars_inner(
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
                        profile_path = '/1Ocb9v3h54beGVoJMm4w50UQhLf.jpg', )
                    ],
                name = 'Winter Is Coming',
                overview = 'Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.',
                id = 63056,
                production_code = '101',
                runtime = 62,
                season_number = 1,
                still_path = '/9hGF3WUkBf7cSjMg0cdMDHJkByd.jpg',
                vote_average = 7.8,
                vote_count = 286
            )
        else:
            return TvEpisodeDetails200Response(
        )
        """

    def testTvEpisodeDetails200Response(self):
        """Test TvEpisodeDetails200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()