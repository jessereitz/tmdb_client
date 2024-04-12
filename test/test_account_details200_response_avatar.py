# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.account_details200_response_avatar import AccountDetails200ResponseAvatar

class TestAccountDetails200ResponseAvatar(unittest.TestCase):
    """AccountDetails200ResponseAvatar unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountDetails200ResponseAvatar:
        """Test AccountDetails200ResponseAvatar
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountDetails200ResponseAvatar`
        """
        model = AccountDetails200ResponseAvatar()
        if include_optional:
            return AccountDetails200ResponseAvatar(
                gravatar = tmdb_client.models.account_details_200_response_avatar_gravatar.account_details_200_response_avatar_gravatar(
                    hash = 'c9e9fc152ee756a900db85757c29815d', ),
                tmdb = tmdb_client.models.account_details_200_response_avatar_tmdb.account_details_200_response_avatar_tmdb(
                    avatar_path = '/xy44UvpbTgzs9kWmp4C3fEaCl5h.png', )
            )
        else:
            return AccountDetails200ResponseAvatar(
        )
        """

    def testAccountDetails200ResponseAvatar(self):
        """Test AccountDetails200ResponseAvatar"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
