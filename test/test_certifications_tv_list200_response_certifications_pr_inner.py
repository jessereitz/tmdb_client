# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.certifications_tv_list200_response_certifications_pr_inner import CertificationsTvList200ResponseCertificationsPRInner

class TestCertificationsTvList200ResponseCertificationsPRInner(unittest.TestCase):
    """CertificationsTvList200ResponseCertificationsPRInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificationsTvList200ResponseCertificationsPRInner:
        """Test CertificationsTvList200ResponseCertificationsPRInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificationsTvList200ResponseCertificationsPRInner`
        """
        model = CertificationsTvList200ResponseCertificationsPRInner()
        if include_optional:
            return CertificationsTvList200ResponseCertificationsPRInner(
                certification = 'NR',
                meaning = '',
                order = 0
            )
        else:
            return CertificationsTvList200ResponseCertificationsPRInner(
        )
        """

    def testCertificationsTvList200ResponseCertificationsPRInner(self):
        """Test CertificationsTvList200ResponseCertificationsPRInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
