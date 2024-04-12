# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_top_rated_list200_response import TvSeriesTopRatedList200Response

class TestTvSeriesTopRatedList200Response(unittest.TestCase):
    """TvSeriesTopRatedList200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesTopRatedList200Response:
        """Test TvSeriesTopRatedList200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesTopRatedList200Response`
        """
        model = TvSeriesTopRatedList200Response()
        if include_optional:
            return TvSeriesTopRatedList200Response(
                page = 1,
                results = [
                    tmdb_client.models.tv_series_top_rated_list_200_response_results_inner.tv_series_top_rated_list_200_response_results_inner(
                        backdrop_path = '/99vBORZixICa32Pwdwj0lWcr8K.jpg', 
                        first_air_date = '2021-09-03', 
                        genre_ids = [
                            10764
                            ], 
                        id = 130392, 
                        name = 'The D'Amelio Show', 
                        origin_country = [
                            'US'
                            ], 
                        original_language = 'en', 
                        original_name = 'The D'Amelio Show', 
                        overview = 'From relative obscurity and a seemingly normal life, to overnight success and thrust into the Hollywood limelight overnight, the D’Amelios are faced with new challenges and opportunities they could not have imagined.', 
                        popularity = 12.459, 
                        poster_path = '/phv2Jc4H8cvRzvTKb9X1uKMboTu.jpg', 
                        vote_average = 8.9, 
                        vote_count = 3190, )
                    ],
                total_pages = 142,
                total_results = 2833
            )
        else:
            return TvSeriesTopRatedList200Response(
        )
        """

    def testTvSeriesTopRatedList200Response(self):
        """Test TvSeriesTopRatedList200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
