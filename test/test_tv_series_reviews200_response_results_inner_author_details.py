# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_reviews200_response_results_inner_author_details import TvSeriesReviews200ResponseResultsInnerAuthorDetails

class TestTvSeriesReviews200ResponseResultsInnerAuthorDetails(unittest.TestCase):
    """TvSeriesReviews200ResponseResultsInnerAuthorDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesReviews200ResponseResultsInnerAuthorDetails:
        """Test TvSeriesReviews200ResponseResultsInnerAuthorDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesReviews200ResponseResultsInnerAuthorDetails`
        """
        model = TvSeriesReviews200ResponseResultsInnerAuthorDetails()
        if include_optional:
            return TvSeriesReviews200ResponseResultsInnerAuthorDetails(
                name = 'lmao7',
                username = 'lmao7',
                avatar_path = '/ekmYOUU4tfx9zGGadjRdE7UPce.jpg',
                rating = 9
            )
        else:
            return TvSeriesReviews200ResponseResultsInnerAuthorDetails(
        )
        """

    def testTvSeriesReviews200ResponseResultsInnerAuthorDetails(self):
        """Test TvSeriesReviews200ResponseResultsInnerAuthorDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
