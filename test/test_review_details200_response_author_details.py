# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.review_details200_response_author_details import ReviewDetails200ResponseAuthorDetails

class TestReviewDetails200ResponseAuthorDetails(unittest.TestCase):
    """ReviewDetails200ResponseAuthorDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReviewDetails200ResponseAuthorDetails:
        """Test ReviewDetails200ResponseAuthorDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReviewDetails200ResponseAuthorDetails`
        """
        model = ReviewDetails200ResponseAuthorDetails()
        if include_optional:
            return ReviewDetails200ResponseAuthorDetails(
                name = 'Ricardo Oliveira',
                username = 'RSOliveira',
                avatar_path = '/23Cl7rhsknc7IIAcZZAGKzovjTu.jpg',
                rating = 9
            )
        else:
            return ReviewDetails200ResponseAuthorDetails(
        )
        """

    def testReviewDetails200ResponseAuthorDetails(self):
        """Test ReviewDetails200ResponseAuthorDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
