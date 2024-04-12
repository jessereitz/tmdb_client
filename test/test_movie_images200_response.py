# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.movie_images200_response import MovieImages200Response

class TestMovieImages200Response(unittest.TestCase):
    """MovieImages200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieImages200Response:
        """Test MovieImages200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieImages200Response`
        """
        model = MovieImages200Response()
        if include_optional:
            return MovieImages200Response(
                backdrops = [
                    openapi_client.models.movie_images_200_response_backdrops_inner.movie_images_200_response_backdrops_inner(
                        aspect_ratio = 1.778, 
                        height = 800, 
                        iso_639_1 = null, 
                        file_path = '/hZkgoQYus5vegHoetLkCJzb17zJ.jpg', 
                        vote_average = 5.622, 
                        vote_count = 20, 
                        width = 1422, )
                    ],
                id = 550,
                logos = [
                    openapi_client.models.movie_images_200_response_logos_inner.movie_images_200_response_logos_inner(
                        aspect_ratio = 5.203, 
                        height = 79, 
                        iso_639_1 = 'he', 
                        file_path = '/c1KLulrIhUqY5fT42nmC5aERGCp.png', 
                        vote_average = 5.312, 
                        vote_count = 1, 
                        width = 411, )
                    ],
                posters = [
                    openapi_client.models.movie_images_200_response_posters_inner.movie_images_200_response_posters_inner(
                        aspect_ratio = 0.667, 
                        height = 900, 
                        iso_639_1 = 'pt', 
                        file_path = '/r3pPehX4ik8NLYPpbDRAh0YRtMb.jpg', 
                        vote_average = 5.258, 
                        vote_count = 6, 
                        width = 600, )
                    ]
            )
        else:
            return MovieImages200Response(
        )
        """

    def testMovieImages200Response(self):
        """Test MovieImages200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
