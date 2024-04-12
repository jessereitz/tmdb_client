# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.movie_account_states200_response import MovieAccountStates200Response

class TestMovieAccountStates200Response(unittest.TestCase):
    """MovieAccountStates200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieAccountStates200Response:
        """Test MovieAccountStates200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieAccountStates200Response`
        """
        model = MovieAccountStates200Response()
        if include_optional:
            return MovieAccountStates200Response(
                id = 550,
                favorite = True,
                rated = openapi_client.models.movie_account_states_200_response_rated.movie_account_states_200_response_rated(
                    value = 9, ),
                watchlist = False
            )
        else:
            return MovieAccountStates200Response(
        )
        """

    def testMovieAccountStates200Response(self):
        """Test MovieAccountStates200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()