# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.alternative_names_copy200_response_logos_inner import AlternativeNamesCopy200ResponseLogosInner

class TestAlternativeNamesCopy200ResponseLogosInner(unittest.TestCase):
    """AlternativeNamesCopy200ResponseLogosInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlternativeNamesCopy200ResponseLogosInner:
        """Test AlternativeNamesCopy200ResponseLogosInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlternativeNamesCopy200ResponseLogosInner`
        """
        model = AlternativeNamesCopy200ResponseLogosInner()
        if include_optional:
            return AlternativeNamesCopy200ResponseLogosInner(
                aspect_ratio = 2.425287356321839,
                file_path = '/tuomPhY2UtuPTqqFnKMVHvSb724.png',
                height = 174,
                id = '5a7a67a40e0a26020a000091',
                file_type = '.svg',
                vote_average = 5.318,
                vote_count = 3,
                width = 422
            )
        else:
            return AlternativeNamesCopy200ResponseLogosInner(
        )
        """

    def testAlternativeNamesCopy200ResponseLogosInner(self):
        """Test AlternativeNamesCopy200ResponseLogosInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
