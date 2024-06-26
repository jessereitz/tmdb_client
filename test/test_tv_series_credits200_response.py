# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_credits200_response import TvSeriesCredits200Response

class TestTvSeriesCredits200Response(unittest.TestCase):
    """TvSeriesCredits200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesCredits200Response:
        """Test TvSeriesCredits200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesCredits200Response`
        """
        model = TvSeriesCredits200Response()
        if include_optional:
            return TvSeriesCredits200Response(
                cast = [
                    tmdb_client.models.tv_series_credits_200_response_cast_inner.tv_series_credits_200_response_cast_inner(
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
                    tmdb_client.models.tv_series_credits_200_response_crew_inner.tv_series_credits_200_response_crew_inner(
                        adult = False, 
                        gender = 2, 
                        id = 1406855, 
                        known_for_department = 'Production', 
                        name = 'Duncan Muggoch', 
                        original_name = 'Duncan Muggoch', 
                        popularity = 1.592, 
                        profile_path = '/ukGjJ62Ejd4cFziald03G34Fsrp.jpg', 
                        credit_id = '5ceab029c3a3682e93217a85', 
                        department = 'Production', 
                        job = 'Producer', )
                    ],
                id = 1399
            )
        else:
            return TvSeriesCredits200Response(
        )
        """

    def testTvSeriesCredits200Response(self):
        """Test TvSeriesCredits200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
