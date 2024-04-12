# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.movie_similar200_response import MovieSimilar200Response

class TestMovieSimilar200Response(unittest.TestCase):
    """MovieSimilar200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MovieSimilar200Response:
        """Test MovieSimilar200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MovieSimilar200Response`
        """
        model = MovieSimilar200Response()
        if include_optional:
            return MovieSimilar200Response(
                page = 1,
                results = [
                    openapi_client.models.movie_similar_200_response_results_inner.movie_similar_200_response_results_inner(
                        adult = False, 
                        backdrop_path = '/3YAldML4EDyoC6RBpzceALigrAZ.jpg', 
                        genre_ids = [
                            18
                            ], 
                        id = 9300, 
                        original_language = 'en', 
                        original_title = 'Orlando', 
                        overview = 'England, 1600. Queen Elizabeth I promises Orlando, a young nobleman obsessed with poetry, that she will grant him land and fortune if he agrees to satisfy a very particular request.', 
                        popularity = 7.768, 
                        poster_path = '/xvz0qZkXXMq3dH2Revxii8drxWc.jpg', 
                        release_date = '1992-12-11', 
                        title = 'Orlando', 
                        video = False, 
                        vote_average = 6.966, 
                        vote_count = 262, )
                    ],
                total_pages = 364,
                total_results = 7269
            )
        else:
            return MovieSimilar200Response(
        )
        """

    def testMovieSimilar200Response(self):
        """Test MovieSimilar200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
