# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_reviews200_response_results_inner_author_details import MovieReviews200ResponseResultsInnerAuthorDetails

class TestMovieReviews200ResponseResultsInnerAuthorDetails(unittest.TestCase):
    """MovieReviews200ResponseResultsInnerAuthorDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieReviews200ResponseResultsInnerAuthorDetails:
        """Test MovieReviews200ResponseResultsInnerAuthorDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieReviews200ResponseResultsInnerAuthorDetails`
        """
        model = MovieReviews200ResponseResultsInnerAuthorDetails()
        if include_optional:
            return MovieReviews200ResponseResultsInnerAuthorDetails(
                name = '',
                username = 'Goddard',
                avatar_path = '/https://secure.gravatar.com/avatar/f248ec34f953bc62cafcbdd81fddd6b6.jpg',
                rating = None
            )
        else:
            return MovieReviews200ResponseResultsInnerAuthorDetails(
        )
        """

    def testMovieReviews200ResponseResultsInnerAuthorDetails(self):
        """Test MovieReviews200ResponseResultsInnerAuthorDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
