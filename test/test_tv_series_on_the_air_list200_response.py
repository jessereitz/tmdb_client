# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_on_the_air_list200_response import TvSeriesOnTheAirList200Response

class TestTvSeriesOnTheAirList200Response(unittest.TestCase):
    """TvSeriesOnTheAirList200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesOnTheAirList200Response:
        """Test TvSeriesOnTheAirList200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesOnTheAirList200Response`
        """
        model = TvSeriesOnTheAirList200Response()
        if include_optional:
            return TvSeriesOnTheAirList200Response(
                page = 1,
                results = [
                    openapi_client.models.tv_series_airing_today_list_200_response_results_inner.tv_series_airing_today_list_200_response_results_inner(
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
                        popularity = 2797.914, 
                        poster_path = '/aoAZgnmMzY9vVy9VWnO3U5PZENh.jpg', 
                        vote_average = 5, 
                        vote_count = 13, )
                    ],
                total_pages = 58,
                total_results = 1151
            )
        else:
            return TvSeriesOnTheAirList200Response(
        )
        """

    def testTvSeriesOnTheAirList200Response(self):
        """Test TvSeriesOnTheAirList200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()