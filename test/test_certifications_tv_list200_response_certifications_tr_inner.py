# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.certifications_tv_list200_response_certifications_tr_inner import CertificationsTvList200ResponseCertificationsTRInner

class TestCertificationsTvList200ResponseCertificationsTRInner(unittest.TestCase):
    """CertificationsTvList200ResponseCertificationsTRInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificationsTvList200ResponseCertificationsTRInner:
        """Test CertificationsTvList200ResponseCertificationsTRInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificationsTvList200ResponseCertificationsTRInner`
        """
        model = CertificationsTvList200ResponseCertificationsTRInner()
        if include_optional:
            return CertificationsTvList200ResponseCertificationsTRInner(
                certification = 'Genel İzleyici',
                meaning = 'General audience. Suitable for all ages.',
                order = 1
            )
        else:
            return CertificationsTvList200ResponseCertificationsTRInner(
        )
        """

    def testCertificationsTvList200ResponseCertificationsTRInner(self):
        """Test CertificationsTvList200ResponseCertificationsTRInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
