# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.movie_credits200_response_crew_inner import MovieCredits200ResponseCrewInner

class TestMovieCredits200ResponseCrewInner(unittest.TestCase):
    """MovieCredits200ResponseCrewInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieCredits200ResponseCrewInner:
        """Test MovieCredits200ResponseCrewInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieCredits200ResponseCrewInner`
        """
        model = MovieCredits200ResponseCrewInner()
        if include_optional:
            return MovieCredits200ResponseCrewInner(
                adult = False,
                gender = 2,
                id = 376,
                known_for_department = 'Production',
                name = 'Arnon Milchan',
                original_name = 'Arnon Milchan',
                popularity = 2.931,
                profile_path = '/b2hBExX4NnczNAnLuTBF4kmNhZm.jpg',
                credit_id = '55731b8192514111610027d7',
                department = 'Production',
                job = 'Executive Producer'
            )
        else:
            return MovieCredits200ResponseCrewInner(
        )
        """

    def testMovieCredits200ResponseCrewInner(self):
        """Test MovieCredits200ResponseCrewInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()