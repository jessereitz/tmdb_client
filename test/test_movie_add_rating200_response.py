# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_add_rating200_response import MovieAddRating200Response

class TestMovieAddRating200Response(unittest.TestCase):
    """MovieAddRating200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieAddRating200Response:
        """Test MovieAddRating200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieAddRating200Response`
        """
        model = MovieAddRating200Response()
        if include_optional:
            return MovieAddRating200Response(
                status_code = 1,
                status_message = 'Success.'
            )
        else:
            return MovieAddRating200Response(
        )
        """

    def testMovieAddRating200Response(self):
        """Test MovieAddRating200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
