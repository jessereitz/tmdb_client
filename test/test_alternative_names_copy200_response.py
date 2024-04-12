# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.alternative_names_copy200_response import AlternativeNamesCopy200Response

class TestAlternativeNamesCopy200Response(unittest.TestCase):
    """AlternativeNamesCopy200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlternativeNamesCopy200Response:
        """Test AlternativeNamesCopy200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlternativeNamesCopy200Response`
        """
        model = AlternativeNamesCopy200Response()
        if include_optional:
            return AlternativeNamesCopy200Response(
                id = 49,
                logos = [
                    openapi_client.models.alternative_names_copy_200_response_logos_inner.alternative_names_copy_200_response_logos_inner(
                        aspect_ratio = 2.425287356321839, 
                        file_path = '/tuomPhY2UtuPTqqFnKMVHvSb724.png', 
                        height = 174, 
                        id = '5a7a67a40e0a26020a000091', 
                        file_type = '.svg', 
                        vote_average = 5.318, 
                        vote_count = 3, 
                        width = 422, )
                    ]
            )
        else:
            return AlternativeNamesCopy200Response(
        )
        """

    def testAlternativeNamesCopy200Response(self):
        """Test AlternativeNamesCopy200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
