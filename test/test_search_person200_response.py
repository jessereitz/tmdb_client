# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.search_person200_response import SearchPerson200Response

class TestSearchPerson200Response(unittest.TestCase):
    """SearchPerson200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchPerson200Response:
        """Test SearchPerson200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchPerson200Response`
        """
        model = SearchPerson200Response()
        if include_optional:
            return SearchPerson200Response(
                page = 1,
                results = [
                    tmdb_client.models.search_person_200_response_results_inner.search_person_200_response_results_inner(
                        adult = False, 
                        gender = 2, 
                        id = 31, 
                        known_for_department = 'Acting', 
                        name = 'Tom Hanks', 
                        original_name = 'Tom Hanks', 
                        popularity = 84.631, 
                        profile_path = '/xndWFsBlClOJFRdhSt4NBwiPq2o.jpg', 
                        known_for = [
                            tmdb_client.models.search_person_200_response_results_inner_known_for_inner.search_person_200_response_results_inner_known_for_inner(
                                adult = False, 
                                backdrop_path = '/3h1JZGDhZ8nzxdgvkxha0qBqi05.jpg', 
                                id = 13, 
                                title = 'Forrest Gump', 
                                original_language = 'en', 
                                original_title = 'Forrest Gump', 
                                overview = 'A man with a low IQ has accomplished great things in his life and been present during significant historic events—in each case, far exceeding what anyone imagined he could do. But despite all he has achieved, his one true love eludes him.', 
                                poster_path = '/arw2vcBveWOVZr6pxd9XTd1TdQa.jpg', 
                                media_type = 'movie', 
                                genre_ids = [
                                    35
                                    ], 
                                popularity = 67.209, 
                                release_date = '1994-06-23', 
                                video = False, 
                                vote_average = 8.481, 
                                vote_count = 24525, )
                            ], )
                    ],
                total_pages = 1,
                total_results = 1
            )
        else:
            return SearchPerson200Response(
        )
        """

    def testSearchPerson200Response(self):
        """Test SearchPerson200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
