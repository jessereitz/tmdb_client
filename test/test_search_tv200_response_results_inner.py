# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.search_tv200_response_results_inner import SearchTv200ResponseResultsInner

class TestSearchTv200ResponseResultsInner(unittest.TestCase):
    """SearchTv200ResponseResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchTv200ResponseResultsInner:
        """Test SearchTv200ResponseResultsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchTv200ResponseResultsInner`
        """
        model = SearchTv200ResponseResultsInner()
        if include_optional:
            return SearchTv200ResponseResultsInner(
                adult = False,
                backdrop_path = '/bsNm9z2TJfe0WO3RedPGWQ8mG1X.jpg',
                genre_ids = [
                    18
                    ],
                id = 1396,
                origin_country = [
                    'US'
                    ],
                original_language = 'en',
                original_name = 'Breaking Bad',
                overview = 'When Walter White, a New Mexico chemistry teacher, is diagnosed with Stage III cancer and given a prognosis of only two years left to live. He becomes filled with a sense of fearlessness and an unrelenting desire to secure his family's financial future at any cost as he enters the dangerous world of drugs and crime.',
                popularity = 298.884,
                poster_path = '/ggFHVNu6YYI5L9pCfOacjizRGt.jpg',
                first_air_date = '2008-01-20',
                name = 'Breaking Bad',
                vote_average = 8.879,
                vote_count = 11536
            )
        else:
            return SearchTv200ResponseResultsInner(
        )
        """

    def testSearchTv200ResponseResultsInner(self):
        """Test SearchTv200ResponseResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()