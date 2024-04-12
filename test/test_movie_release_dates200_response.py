# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.movie_release_dates200_response import MovieReleaseDates200Response

class TestMovieReleaseDates200Response(unittest.TestCase):
    """MovieReleaseDates200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieReleaseDates200Response:
        """Test MovieReleaseDates200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieReleaseDates200Response`
        """
        model = MovieReleaseDates200Response()
        if include_optional:
            return MovieReleaseDates200Response(
                id = 550,
                results = [
                    openapi_client.models.movie_release_dates_200_response_results_inner.movie_release_dates_200_response_results_inner(
                        iso_3166_1 = 'BG', 
                        release_dates = [
                            openapi_client.models.movie_release_dates_200_response_results_inner_release_dates_inner.movie_release_dates_200_response_results_inner_release_dates_inner(
                                certification = 'c', 
                                descriptors = [
                                    ''
                                    ], 
                                iso_639_1 = '', 
                                note = '', 
                                release_date = '2012-08-28T00:00:00.000Z', 
                                type = 3, )
                            ], )
                    ]
            )
        else:
            return MovieReleaseDates200Response(
        )
        """

    def testMovieReleaseDates200Response(self):
        """Test MovieReleaseDates200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()