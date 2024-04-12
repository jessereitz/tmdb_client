# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.collection_images200_response import CollectionImages200Response

class TestCollectionImages200Response(unittest.TestCase):
    """CollectionImages200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CollectionImages200Response:
        """Test CollectionImages200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CollectionImages200Response`
        """
        model = CollectionImages200Response()
        if include_optional:
            return CollectionImages200Response(
                id = 10,
                backdrops = [
                    openapi_client.models.collection_images_200_response_backdrops_inner.collection_images_200_response_backdrops_inner(
                        aspect_ratio = 1.778, 
                        height = 1080, 
                        iso_639_1 = null, 
                        file_path = '/d8duYyyC9J5T825Hg7grmaabfxQ.jpg', 
                        vote_average = 5.464, 
                        vote_count = 30, 
                        width = 1920, )
                    ],
                posters = [
                    openapi_client.models.collection_images_200_response_posters_inner.collection_images_200_response_posters_inner(
                        aspect_ratio = 0.667, 
                        height = 3000, 
                        iso_639_1 = 'en', 
                        file_path = '/r8Ph5MYXL04Qzu4QBbq2KjqwtkQ.jpg', 
                        vote_average = 5.516, 
                        vote_count = 14, 
                        width = 2000, )
                    ]
            )
        else:
            return CollectionImages200Response(
        )
        """

    def testCollectionImages200Response(self):
        """Test CollectionImages200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()