# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.discover_tv200_response import DiscoverTv200Response

class TestDiscoverTv200Response(unittest.TestCase):
    """DiscoverTv200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DiscoverTv200Response:
        """Test DiscoverTv200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiscoverTv200Response`
        """
        model = DiscoverTv200Response()
        if include_optional:
            return DiscoverTv200Response(
                page = 1,
                results = [
                    tmdb_client.models.discover_tv_200_response_results_inner.discover_tv_200_response_results_inner(
                        backdrop_path = '/mAJ84W6I8I272Da87qplS2Dp9ST.jpg', 
                        first_air_date = '2023-01-23', 
                        genre_ids = [
                            9648
                            ], 
                        id = 202250, 
                        name = 'Dirty Linen', 
                        origin_country = [
                            'PH'
                            ], 
                        original_language = 'tl', 
                        original_name = 'Dirty Linen', 
                        overview = 'To exact vengeance, a young woman infiltrates the household of an influential family as a housemaid to expose their dirty secrets. However, love will get in the way of her revenge plot.', 
                        popularity = 2684.061, 
                        poster_path = '/ujlkQtHAVShWyWTloGU2Vh5Jbo9.jpg', 
                        vote_average = 5, 
                        vote_count = 13, )
                    ],
                total_pages = 7414,
                total_results = 148265
            )
        else:
            return DiscoverTv200Response(
        )
        """

    def testDiscoverTv200Response(self):
        """Test DiscoverTv200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
