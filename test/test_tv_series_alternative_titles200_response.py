# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_alternative_titles200_response import TvSeriesAlternativeTitles200Response

class TestTvSeriesAlternativeTitles200Response(unittest.TestCase):
    """TvSeriesAlternativeTitles200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesAlternativeTitles200Response:
        """Test TvSeriesAlternativeTitles200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesAlternativeTitles200Response`
        """
        model = TvSeriesAlternativeTitles200Response()
        if include_optional:
            return TvSeriesAlternativeTitles200Response(
                id = 1399,
                results = [
                    openapi_client.models.tv_series_alternative_titles_200_response_results_inner.tv_series_alternative_titles_200_response_results_inner(
                        iso_3166_1 = 'AL', 
                        title = 'Froni i shpatave', 
                        type = '', )
                    ]
            )
        else:
            return TvSeriesAlternativeTitles200Response(
        )
        """

    def testTvSeriesAlternativeTitles200Response(self):
        """Test TvSeriesAlternativeTitles200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()