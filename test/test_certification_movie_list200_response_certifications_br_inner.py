# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.certification_movie_list200_response_certifications_br_inner import CertificationMovieList200ResponseCertificationsBRInner

class TestCertificationMovieList200ResponseCertificationsBRInner(unittest.TestCase):
    """CertificationMovieList200ResponseCertificationsBRInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificationMovieList200ResponseCertificationsBRInner:
        """Test CertificationMovieList200ResponseCertificationsBRInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificationMovieList200ResponseCertificationsBRInner`
        """
        model = CertificationMovieList200ResponseCertificationsBRInner()
        if include_optional:
            return CertificationMovieList200ResponseCertificationsBRInner(
                certification = '14',
                meaning = 'Not recommended for minors under fourteen. More violent material, stronger sex references and/or nudity.',
                order = 4
            )
        else:
            return CertificationMovieList200ResponseCertificationsBRInner(
        )
        """

    def testCertificationMovieList200ResponseCertificationsBRInner(self):
        """Test CertificationMovieList200ResponseCertificationsBRInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
