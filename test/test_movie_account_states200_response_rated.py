# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.movie_account_states200_response_rated import MovieAccountStates200ResponseRated

class TestMovieAccountStates200ResponseRated(unittest.TestCase):
    """MovieAccountStates200ResponseRated unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieAccountStates200ResponseRated:
        """Test MovieAccountStates200ResponseRated
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieAccountStates200ResponseRated`
        """
        model = MovieAccountStates200ResponseRated()
        if include_optional:
            return MovieAccountStates200ResponseRated(
                value = 9
            )
        else:
            return MovieAccountStates200ResponseRated(
        )
        """

    def testMovieAccountStates200ResponseRated(self):
        """Test MovieAccountStates200ResponseRated"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
