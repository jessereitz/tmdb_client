# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_credits200_response import MovieCredits200Response

class TestMovieCredits200Response(unittest.TestCase):
    """MovieCredits200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieCredits200Response:
        """Test MovieCredits200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieCredits200Response`
        """
        model = MovieCredits200Response()
        if include_optional:
            return MovieCredits200Response(
                id = 550,
                cast = [
                    tmdb_client.models.movie_credits_200_response_cast_inner.movie_credits_200_response_cast_inner(
                        adult = False, 
                        gender = 2, 
                        id = 819, 
                        known_for_department = 'Acting', 
                        name = 'Edward Norton', 
                        original_name = 'Edward Norton', 
                        popularity = 26.99, 
                        profile_path = '/8nytsqL59SFJTVYVrN72k6qkGgJ.jpg', 
                        cast_id = 4, 
                        character = 'The Narrator', 
                        credit_id = '52fe4250c3a36847f80149f3', 
                        order = 0, )
                    ],
                crew = [
                    tmdb_client.models.movie_credits_200_response_crew_inner.movie_credits_200_response_crew_inner(
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
                        job = 'Executive Producer', )
                    ]
            )
        else:
            return MovieCredits200Response(
        )
        """

    def testMovieCredits200Response(self):
        """Test MovieCredits200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
