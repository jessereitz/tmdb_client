# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.certifications_tv_list200_response_certifications_pl_inner import CertificationsTvList200ResponseCertificationsPLInner

class TestCertificationsTvList200ResponseCertificationsPLInner(unittest.TestCase):
    """CertificationsTvList200ResponseCertificationsPLInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificationsTvList200ResponseCertificationsPLInner:
        """Test CertificationsTvList200ResponseCertificationsPLInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificationsTvList200ResponseCertificationsPLInner`
        """
        model = CertificationsTvList200ResponseCertificationsPLInner()
        if include_optional:
            return CertificationsTvList200ResponseCertificationsPLInner(
                certification = '0',
                meaning = 'Positive or neutral view of the world, little to no violence, non-sexual love, and no sexual content.',
                order = 1
            )
        else:
            return CertificationsTvList200ResponseCertificationsPLInner(
        )
        """

    def testCertificationsTvList200ResponseCertificationsPLInner(self):
        """Test CertificationsTvList200ResponseCertificationsPLInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()