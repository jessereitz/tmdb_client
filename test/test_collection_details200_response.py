# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.collection_details200_response import CollectionDetails200Response

class TestCollectionDetails200Response(unittest.TestCase):
    """CollectionDetails200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CollectionDetails200Response:
        """Test CollectionDetails200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CollectionDetails200Response`
        """
        model = CollectionDetails200Response()
        if include_optional:
            return CollectionDetails200Response(
                id = 10,
                name = 'Star Wars Collection',
                overview = 'An epic space-opera theatrical film series, which depicts the adventures of various characters "a long time ago in a galaxy far, far away…."',
                poster_path = '/r8Ph5MYXL04Qzu4QBbq2KjqwtkQ.jpg',
                backdrop_path = '/d8duYyyC9J5T825Hg7grmaabfxQ.jpg',
                parts = [
                    openapi_client.models.collection_details_200_response_parts_inner.collection_details_200_response_parts_inner(
                        adult = False, 
                        backdrop_path = '/2w4xG178RpB4MDAIfTkqAuSJzec.jpg', 
                        id = 11, 
                        title = 'Star Wars', 
                        original_language = 'en', 
                        original_title = 'Star Wars', 
                        overview = 'Princess Leia is captured and held hostage by the evil Imperial forces in their effort to take over the galactic Empire. Venturesome Luke Skywalker and dashing captain Han Solo team together with the loveable robot duo R2-D2 and C-3PO to rescue the beautiful princess and restore peace and justice in the Empire.', 
                        poster_path = '/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg', 
                        media_type = 'movie', 
                        genre_ids = [
                            12
                            ], 
                        popularity = 100.492, 
                        release_date = '1977-05-25', 
                        video = False, 
                        vote_average = 8.207, 
                        vote_count = 18549, )
                    ]
            )
        else:
            return CollectionDetails200Response(
        )
        """

    def testCollectionDetails200Response(self):
        """Test CollectionDetails200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()