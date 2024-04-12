# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.certification_movie_list200_response_certifications_sk_inner import CertificationMovieList200ResponseCertificationsSKInner

class TestCertificationMovieList200ResponseCertificationsSKInner(unittest.TestCase):
    """CertificationMovieList200ResponseCertificationsSKInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificationMovieList200ResponseCertificationsSKInner:
        """Test CertificationMovieList200ResponseCertificationsSKInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificationMovieList200ResponseCertificationsSKInner`
        """
        model = CertificationMovieList200ResponseCertificationsSKInner()
        if include_optional:
            return CertificationMovieList200ResponseCertificationsSKInner(
                certification = 'U',
                meaning = 'General audience.',
                order = 1
            )
        else:
            return CertificationMovieList200ResponseCertificationsSKInner(
        )
        """

    def testCertificationMovieList200ResponseCertificationsSKInner(self):
        """Test CertificationMovieList200ResponseCertificationsSKInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()