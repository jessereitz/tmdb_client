# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_similar200_response import TvSeriesSimilar200Response

class TestTvSeriesSimilar200Response(unittest.TestCase):
    """TvSeriesSimilar200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesSimilar200Response:
        """Test TvSeriesSimilar200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesSimilar200Response`
        """
        model = TvSeriesSimilar200Response()
        if include_optional:
            return TvSeriesSimilar200Response(
                page = 1,
                results = [
                    openapi_client.models.tv_series_similar_200_response_results_inner.tv_series_similar_200_response_results_inner(
                        adult = False, 
                        backdrop_path = '/zcFSvWa34nDn2NcqOPuthyOIBWT.jpg', 
                        genre_ids = [
                            18
                            ], 
                        id = 197063, 
                        origin_country = [
                            'KR'
                            ], 
                        original_language = 'ko', 
                        original_name = '종이달', 
                        overview = 'A thriller drama about Yoo I-hwa, a stay-at-home mom living her comfortable and contented life without desires, but to her husband's indifference. While working as a bank contract employee, she unexpectedly touches money from VIP clients and gradually falls into an irreversible collapse.', 
                        popularity = 12.299, 
                        poster_path = '/xXWynVdMGyJXBUDvIN27AXM3iJJ.jpg', 
                        first_air_date = '2023-04-10', 
                        name = 'Pale Moon', 
                        vote_average = 7, 
                        vote_count = 2, )
                    ],
                total_pages = 82,
                total_results = 1639
            )
        else:
            return TvSeriesSimilar200Response(
        )
        """

    def testTvSeriesSimilar200Response(self):
        """Test TvSeriesSimilar200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()