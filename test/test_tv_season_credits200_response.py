# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_season_credits200_response import TvSeasonCredits200Response

class TestTvSeasonCredits200Response(unittest.TestCase):
    """TvSeasonCredits200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeasonCredits200Response:
        """Test TvSeasonCredits200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeasonCredits200Response`
        """
        model = TvSeasonCredits200Response()
        if include_optional:
            return TvSeasonCredits200Response(
                cast = [
                    openapi_client.models.tv_series_credits_200_response_cast_inner.tv_series_credits_200_response_cast_inner(
                        adult = False, 
                        gender = 2, 
                        id = 22970, 
                        known_for_department = 'Acting', 
                        name = 'Peter Dinklage', 
                        original_name = 'Peter Dinklage', 
                        popularity = 30.6, 
                        profile_path = '/lRsRgnksAhBRXwAB68MFjmTtLrk.jpg', 
                        character = 'Tyrion Lannister', 
                        credit_id = '5256c8b219c2956ff6047cd8', 
                        order = 0, )
                    ],
                crew = [
                    openapi_client.models.tv_season_credits_200_response_crew_inner.tv_season_credits_200_response_crew_inner(
                        adult = False, 
                        gender = 0, 
                        id = 1223796, 
                        known_for_department = 'Production', 
                        name = 'Frank Doelger', 
                        original_name = 'Frank Doelger', 
                        popularity = 0.694, 
                        profile_path = null, 
                        credit_id = '5256c8c419c2956ff604867c', 
                        department = 'Production', 
                        job = 'Producer', )
                    ],
                id = 3624
            )
        else:
            return TvSeasonCredits200Response(
        )
        """

    def testTvSeasonCredits200Response(self):
        """Test TvSeasonCredits200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()