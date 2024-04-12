# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.certification_movie_list200_response_certifications_id_inner import CertificationMovieList200ResponseCertificationsIDInner

class TestCertificationMovieList200ResponseCertificationsIDInner(unittest.TestCase):
    """CertificationMovieList200ResponseCertificationsIDInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificationMovieList200ResponseCertificationsIDInner:
        """Test CertificationMovieList200ResponseCertificationsIDInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificationMovieList200ResponseCertificationsIDInner`
        """
        model = CertificationMovieList200ResponseCertificationsIDInner()
        if include_optional:
            return CertificationMovieList200ResponseCertificationsIDInner(
                certification = 'SU',
                meaning = 'All ages.',
                order = 1
            )
        else:
            return CertificationMovieList200ResponseCertificationsIDInner(
        )
        """

    def testCertificationMovieList200ResponseCertificationsIDInner(self):
        """Test CertificationMovieList200ResponseCertificationsIDInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()