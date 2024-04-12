# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.movie_delete_rating200_response import MovieDeleteRating200Response

class TestMovieDeleteRating200Response(unittest.TestCase):
    """MovieDeleteRating200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieDeleteRating200Response:
        """Test MovieDeleteRating200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieDeleteRating200Response`
        """
        model = MovieDeleteRating200Response()
        if include_optional:
            return MovieDeleteRating200Response(
                status_code = 13,
                status_message = 'The item/record was deleted successfully.'
            )
        else:
            return MovieDeleteRating200Response(
        )
        """

    def testMovieDeleteRating200Response(self):
        """Test MovieDeleteRating200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
