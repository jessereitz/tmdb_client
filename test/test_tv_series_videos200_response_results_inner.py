# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_videos200_response_results_inner import TvSeriesVideos200ResponseResultsInner

class TestTvSeriesVideos200ResponseResultsInner(unittest.TestCase):
    """TvSeriesVideos200ResponseResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesVideos200ResponseResultsInner:
        """Test TvSeriesVideos200ResponseResultsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesVideos200ResponseResultsInner`
        """
        model = TvSeriesVideos200ResponseResultsInner()
        if include_optional:
            return TvSeriesVideos200ResponseResultsInner(
                iso_639_1 = 'en',
                iso_3166_1 = 'US',
                name = 'Inside Game of Thrones: A Story in Camera Work – BTS (HBO)',
                key = 'y2ZJ3lTaREY',
                site = 'YouTube',
                size = 1080,
                type = 'Behind the Scenes',
                official = True,
                published_at = '2019-03-25T14:00:06.000Z',
                id = '5c999b48c3a36863b73b9d42'
            )
        else:
            return TvSeriesVideos200ResponseResultsInner(
        )
        """

    def testTvSeriesVideos200ResponseResultsInner(self):
        """Test TvSeriesVideos200ResponseResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
