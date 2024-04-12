# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.search_collection200_response_results_inner import SearchCollection200ResponseResultsInner

class TestSearchCollection200ResponseResultsInner(unittest.TestCase):
    """SearchCollection200ResponseResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchCollection200ResponseResultsInner:
        """Test SearchCollection200ResponseResultsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchCollection200ResponseResultsInner`
        """
        model = SearchCollection200ResponseResultsInner()
        if include_optional:
            return SearchCollection200ResponseResultsInner(
                adult = False,
                backdrop_path = '/zuW6fOiusv4X9nnW3paHGfXcSll.jpg',
                id = 86311,
                name = 'The Avengers Collection',
                original_language = 'en',
                original_name = 'The Avengers Collection',
                overview = 'A superhero film series produced by Marvel Studios based on the Marvel Comics superhero team of the same name, and part of the Marvel Cinematic Universe (MCU).  The series features an ensemble cast from the Marvel Cinematic Universe series films, as they join forces for the peacekeeping organization S.H.I.E.L.D. led by Nick Fury.',
                poster_path = '/yFSIUVTCvgYrpalUktulvk3Gi5Y.jpg'
            )
        else:
            return SearchCollection200ResponseResultsInner(
        )
        """

    def testSearchCollection200ResponseResultsInner(self):
        """Test SearchCollection200ResponseResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
