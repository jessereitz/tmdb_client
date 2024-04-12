# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.guest_session_rated_tv_episodes200_response import GuestSessionRatedTvEpisodes200Response

class TestGuestSessionRatedTvEpisodes200Response(unittest.TestCase):
    """GuestSessionRatedTvEpisodes200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GuestSessionRatedTvEpisodes200Response:
        """Test GuestSessionRatedTvEpisodes200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GuestSessionRatedTvEpisodes200Response`
        """
        model = GuestSessionRatedTvEpisodes200Response()
        if include_optional:
            return GuestSessionRatedTvEpisodes200Response(
                page = 1,
                results = [
                    openapi_client.models.guest_session_rated_tv_episodes_200_response_results_inner.guest_session_rated_tv_episodes_200_response_results_inner(
                        air_date = '2011-04-17', 
                        episode_number = 1, 
                        id = 63056, 
                        name = 'Winter Is Coming', 
                        overview = 'Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.', 
                        production_code = '101', 
                        runtime = 62, 
                        season_number = 1, 
                        show_id = 1399, 
                        still_path = '/9hGF3WUkBf7cSjMg0cdMDHJkByd.jpg', 
                        vote_average = 7.843, 
                        vote_count = 286, 
                        rating = 8.5, )
                    ],
                total_pages = 1,
                total_results = 1
            )
        else:
            return GuestSessionRatedTvEpisodes200Response(
        )
        """

    def testGuestSessionRatedTvEpisodes200Response(self):
        """Test GuestSessionRatedTvEpisodes200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
