# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.person_external_ids200_response import PersonExternalIds200Response

class TestPersonExternalIds200Response(unittest.TestCase):
    """PersonExternalIds200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PersonExternalIds200Response:
        """Test PersonExternalIds200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PersonExternalIds200Response`
        """
        model = PersonExternalIds200Response()
        if include_optional:
            return PersonExternalIds200Response(
                id = 31,
                freebase_mid = '/m/0bxtg',
                freebase_id = '/en/tom_hanks',
                imdb_id = 'nm0000158',
                tvrage_id = 14293,
                wikidata_id = 'Q2263',
                facebook_id = 'TomHanks',
                instagram_id = 'tomhanks',
                tiktok_id = 'tomhanks',
                twitter_id = 'tomhanks',
                youtube_id = None
            )
        else:
            return PersonExternalIds200Response(
        )
        """

    def testPersonExternalIds200Response(self):
        """Test PersonExternalIds200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
