# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.collection_images200_response_backdrops_inner import CollectionImages200ResponseBackdropsInner

class TestCollectionImages200ResponseBackdropsInner(unittest.TestCase):
    """CollectionImages200ResponseBackdropsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CollectionImages200ResponseBackdropsInner:
        """Test CollectionImages200ResponseBackdropsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CollectionImages200ResponseBackdropsInner`
        """
        model = CollectionImages200ResponseBackdropsInner()
        if include_optional:
            return CollectionImages200ResponseBackdropsInner(
                aspect_ratio = 1.778,
                height = 1080,
                iso_639_1 = None,
                file_path = '/d8duYyyC9J5T825Hg7grmaabfxQ.jpg',
                vote_average = 5.464,
                vote_count = 30,
                width = 1920
            )
        else:
            return CollectionImages200ResponseBackdropsInner(
        )
        """

    def testCollectionImages200ResponseBackdropsInner(self):
        """Test CollectionImages200ResponseBackdropsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()