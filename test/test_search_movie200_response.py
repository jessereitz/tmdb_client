# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.search_movie200_response import SearchMovie200Response

class TestSearchMovie200Response(unittest.TestCase):
    """SearchMovie200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchMovie200Response:
        """Test SearchMovie200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchMovie200Response`
        """
        model = SearchMovie200Response()
        if include_optional:
            return SearchMovie200Response(
                page = 1,
                results = [
                    openapi_client.models.search_movie_200_response_results_inner.search_movie_200_response_results_inner(
                        adult = False, 
                        backdrop_path = '/hZkgoQYus5vegHoetLkCJzb17zJ.jpg', 
                        genre_ids = [
                            18
                            ], 
                        id = 550, 
                        original_language = 'en', 
                        original_title = 'Fight Club', 
                        overview = 'A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground "fight clubs" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.', 
                        popularity = 73.433, 
                        poster_path = '/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg', 
                        release_date = '1999-10-15', 
                        title = 'Fight Club', 
                        video = False, 
                        vote_average = 8.433, 
                        vote_count = 26279, )
                    ],
                total_pages = 2,
                total_results = 39
            )
        else:
            return SearchMovie200Response(
        )
        """

    def testSearchMovie200Response(self):
        """Test SearchMovie200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
