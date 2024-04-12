# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.collection_translations200_response import CollectionTranslations200Response

class TestCollectionTranslations200Response(unittest.TestCase):
    """CollectionTranslations200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CollectionTranslations200Response:
        """Test CollectionTranslations200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CollectionTranslations200Response`
        """
        model = CollectionTranslations200Response()
        if include_optional:
            return CollectionTranslations200Response(
                id = 10,
                translations = [
                    openapi_client.models.collection_translations_200_response_translations_inner.collection_translations_200_response_translations_inner(
                        iso_3166_1 = 'AE', 
                        iso_639_1 = 'ar', 
                        name = 'العربية', 
                        english_name = 'Arabic', 
                        data = openapi_client.models.collection_translations_200_response_translations_inner_data.collection_translations_200_response_translations_inner_data(
                            title = '', 
                            overview = '', 
                            homepage = '', ), )
                    ]
            )
        else:
            return CollectionTranslations200Response(
        )
        """

    def testCollectionTranslations200Response(self):
        """Test CollectionTranslations200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()