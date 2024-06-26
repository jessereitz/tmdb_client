# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.certifications_tv_list200_response_certifications_my_inner import CertificationsTvList200ResponseCertificationsMYInner

class TestCertificationsTvList200ResponseCertificationsMYInner(unittest.TestCase):
    """CertificationsTvList200ResponseCertificationsMYInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificationsTvList200ResponseCertificationsMYInner:
        """Test CertificationsTvList200ResponseCertificationsMYInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificationsTvList200ResponseCertificationsMYInner`
        """
        model = CertificationsTvList200ResponseCertificationsMYInner()
        if include_optional:
            return CertificationsTvList200ResponseCertificationsMYInner(
                certification = 'U',
                meaning = 'No age limit. Can be broadcast anytime.',
                order = 1
            )
        else:
            return CertificationsTvList200ResponseCertificationsMYInner(
        )
        """

    def testCertificationsTvList200ResponseCertificationsMYInner(self):
        """Test CertificationsTvList200ResponseCertificationsMYInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
