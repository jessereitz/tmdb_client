# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.certifications_tv_list200_response_certifications_se_inner import CertificationsTvList200ResponseCertificationsSEInner

class TestCertificationsTvList200ResponseCertificationsSEInner(unittest.TestCase):
    """CertificationsTvList200ResponseCertificationsSEInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificationsTvList200ResponseCertificationsSEInner:
        """Test CertificationsTvList200ResponseCertificationsSEInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificationsTvList200ResponseCertificationsSEInner`
        """
        model = CertificationsTvList200ResponseCertificationsSEInner()
        if include_optional:
            return CertificationsTvList200ResponseCertificationsSEInner(
                certification = 'Btl',
                meaning = '',
                order = 1
            )
        else:
            return CertificationsTvList200ResponseCertificationsSEInner(
        )
        """

    def testCertificationsTvList200ResponseCertificationsSEInner(self):
        """Test CertificationsTvList200ResponseCertificationsSEInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
