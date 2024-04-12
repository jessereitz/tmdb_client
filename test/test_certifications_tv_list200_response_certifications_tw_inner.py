# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.certifications_tv_list200_response_certifications_tw_inner import CertificationsTvList200ResponseCertificationsTWInner

class TestCertificationsTvList200ResponseCertificationsTWInner(unittest.TestCase):
    """CertificationsTvList200ResponseCertificationsTWInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificationsTvList200ResponseCertificationsTWInner:
        """Test CertificationsTvList200ResponseCertificationsTWInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificationsTvList200ResponseCertificationsTWInner`
        """
        model = CertificationsTvList200ResponseCertificationsTWInner()
        if include_optional:
            return CertificationsTvList200ResponseCertificationsTWInner(
                certification = '0+',
                meaning = 'Suitable for watching by general audiences.',
                order = 1
            )
        else:
            return CertificationsTvList200ResponseCertificationsTWInner(
        )
        """

    def testCertificationsTvList200ResponseCertificationsTWInner(self):
        """Test CertificationsTvList200ResponseCertificationsTWInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
