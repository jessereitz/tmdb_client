# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.certifications_tv_list200_response_certifications_pt_inner import CertificationsTvList200ResponseCertificationsPTInner

class TestCertificationsTvList200ResponseCertificationsPTInner(unittest.TestCase):
    """CertificationsTvList200ResponseCertificationsPTInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificationsTvList200ResponseCertificationsPTInner:
        """Test CertificationsTvList200ResponseCertificationsPTInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificationsTvList200ResponseCertificationsPTInner`
        """
        model = CertificationsTvList200ResponseCertificationsPTInner()
        if include_optional:
            return CertificationsTvList200ResponseCertificationsPTInner(
                certification = '12AP',
                meaning = 'Acompanhamento Parental (may not be suitable for children under 12, parental guidance advised).',
                order = 3
            )
        else:
            return CertificationsTvList200ResponseCertificationsPTInner(
        )
        """

    def testCertificationsTvList200ResponseCertificationsPTInner(self):
        """Test CertificationsTvList200ResponseCertificationsPTInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
