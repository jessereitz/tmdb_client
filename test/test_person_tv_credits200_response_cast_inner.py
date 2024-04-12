# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.person_tv_credits200_response_cast_inner import PersonTvCredits200ResponseCastInner

class TestPersonTvCredits200ResponseCastInner(unittest.TestCase):
    """PersonTvCredits200ResponseCastInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PersonTvCredits200ResponseCastInner:
        """Test PersonTvCredits200ResponseCastInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PersonTvCredits200ResponseCastInner`
        """
        model = PersonTvCredits200ResponseCastInner()
        if include_optional:
            return PersonTvCredits200ResponseCastInner(
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
                episode_count = 1
            )
        else:
            return PersonTvCredits200ResponseCastInner(
        )
        """

    def testPersonTvCredits200ResponseCastInner(self):
        """Test PersonTvCredits200ResponseCastInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()