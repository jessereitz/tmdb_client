# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.movie_popular_list200_response import MoviePopularList200Response

class TestMoviePopularList200Response(unittest.TestCase):
    """MoviePopularList200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MoviePopularList200Response:
        """Test MoviePopularList200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MoviePopularList200Response`
        """
        model = MoviePopularList200Response()
        if include_optional:
            return MoviePopularList200Response(
                page = 1,
                results = [
                    openapi_client.models.movie_popular_list_200_response_results_inner.movie_popular_list_200_response_results_inner(
                        adult = False, 
                        backdrop_path = '/gMJngTNfaqCSCqGD4y8lVMZXKDn.jpg', 
                        genre_ids = [
                            28
                            ], 
                        id = 640146, 
                        original_language = 'en', 
                        original_title = 'Ant-Man and the Wasp: Quantumania', 
                        overview = 'Super-Hero partners Scott Lang and Hope van Dyne, along with with Hope's parents Janet van Dyne and Hank Pym, and Scott's daughter Cassie Lang, find themselves exploring the Quantum Realm, interacting with strange new creatures and embarking on an adventure that will push them beyond the limits of what they thought possible.', 
                        popularity = 8567.865, 
                        poster_path = '/ngl2FKBlU4fhbdsrtdom9LVLBXw.jpg', 
                        release_date = '2023-02-15', 
                        title = 'Ant-Man and the Wasp: Quantumania', 
                        video = False, 
                        vote_average = 6.5, 
                        vote_count = 1886, )
                    ],
                total_pages = 38029,
                total_results = 760569
            )
        else:
            return MoviePopularList200Response(
        )
        """

    def testMoviePopularList200Response(self):
        """Test MoviePopularList200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
