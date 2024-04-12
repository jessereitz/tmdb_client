# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_credits200_response_cast_inner import TvSeriesCredits200ResponseCastInner

class TestTvSeriesCredits200ResponseCastInner(unittest.TestCase):
    """TvSeriesCredits200ResponseCastInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesCredits200ResponseCastInner:
        """Test TvSeriesCredits200ResponseCastInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesCredits200ResponseCastInner`
        """
        model = TvSeriesCredits200ResponseCastInner()
        if include_optional:
            return TvSeriesCredits200ResponseCastInner(
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
                order = 0
            )
        else:
            return TvSeriesCredits200ResponseCastInner(
        )
        """

    def testTvSeriesCredits200ResponseCastInner(self):
        """Test TvSeriesCredits200ResponseCastInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
