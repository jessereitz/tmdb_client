# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.movie_reviews200_response import MovieReviews200Response

class TestMovieReviews200Response(unittest.TestCase):
    """MovieReviews200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieReviews200Response:
        """Test MovieReviews200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieReviews200Response`
        """
        model = MovieReviews200Response()
        if include_optional:
            return MovieReviews200Response(
                id = 550,
                page = 1,
                results = [
                    tmdb_client.models.movie_reviews_200_response_results_inner.movie_reviews_200_response_results_inner(
                        author = 'Goddard', 
                        author_details = tmdb_client.models.movie_reviews_200_response_results_inner_author_details.movie_reviews_200_response_results_inner_author_details(
                            name = '', 
                            username = 'Goddard', 
                            avatar_path = '/https://secure.gravatar.com/avatar/f248ec34f953bc62cafcbdd81fddd6b6.jpg', 
                            rating = null, ), 
                        content = 'Pretty awesome movie.  It shows what one crazy person can convince other crazy people to do.  Everyone needs something to believe in.  I recommend Jesus Christ, but they want Tyler Durden.', 
                        created_at = '2018-06-09T17:51:53.359Z', 
                        id = '5b1c13b9c3a36848f2026384', 
                        updated_at = '2021-06-23T15:58:09.421Z', 
                        url = 'https://www.themoviedb.org/review/5b1c13b9c3a36848f2026384', )
                    ],
                total_pages = 1,
                total_results = 8
            )
        else:
            return MovieReviews200Response(
        )
        """

    def testMovieReviews200Response(self):
        """Test MovieReviews200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
