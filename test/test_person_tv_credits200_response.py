# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.person_tv_credits200_response import PersonTvCredits200Response

class TestPersonTvCredits200Response(unittest.TestCase):
    """PersonTvCredits200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PersonTvCredits200Response:
        """Test PersonTvCredits200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PersonTvCredits200Response`
        """
        model = PersonTvCredits200Response()
        if include_optional:
            return PersonTvCredits200Response(
                cast = [
                    tmdb_client.models.person_tv_credits_200_response_cast_inner.person_tv_credits_200_response_cast_inner(
                        adult = False, 
                        backdrop_path = '/ttvojTMgaIN7U8gqB5LlNqO4vPN.jpg', 
                        genre_ids = [
                            10767
                            ], 
                        id = 1900, 
                        origin_country = [
                            'US'
                            ], 
                        original_language = 'en', 
                        original_name = 'LIVE with Kelly and Mark', 
                        overview = 'A morning talk show with A-list celebrity guests, top-notch performances and one-of-a-kind segments that are unrivaled on daytime television, plus spontaneous, hilarious and unpredictable talk.', 
                        popularity = 700.508, 
                        poster_path = '/l5y8egG27p2fSTyq8s21SQMmQLy.jpg', 
                        first_air_date = '1988-09-05', 
                        name = 'LIVE with Kelly and Mark', 
                        vote_average = 5.4, 
                        vote_count = 25, 
                        character = '', 
                        credit_id = '52571af019c29571140d5c92', 
                        episode_count = 1, )
                    ],
                crew = [
                    tmdb_client.models.person_tv_credits_200_response_crew_inner.person_tv_credits_200_response_crew_inner(
                        adult = False, 
                        backdrop_path = '/6uMA6EAiwcsCqQJwWgYwtORvE0v.jpg', 
                        genre_ids = [
                            35
                            ], 
                        id = 2391, 
                        origin_country = [
                            'US'
                            ], 
                        original_language = 'en', 
                        original_name = 'Tales from the Crypt', 
                        overview = 'Cadaverous scream legend the Crypt Keeper is your macabre host for these forays of fright and fun based on the classic E.C. Comics tales from back in the day. So shamble up to the bar and pick your poison. Will it be an insane Santa on a personal slay ride? Honeymooners out to fulfill the "til death do we part" vow ASAP?', 
                        popularity = 24.88, 
                        poster_path = '/dDfXQH6Kg2JNASI0dqNALukjhk1.jpg', 
                        first_air_date = '1989-06-10', 
                        name = 'Tales from the Crypt', 
                        vote_average = 7.978, 
                        vote_count = 757, 
                        credit_id = '525734f3760ee3776a397211', 
                        department = 'Directing', 
                        episode_count = 1, 
                        job = 'Director', )
                    ],
                id = 31
            )
        else:
            return PersonTvCredits200Response(
        )
        """

    def testPersonTvCredits200Response(self):
        """Test PersonTvCredits200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
