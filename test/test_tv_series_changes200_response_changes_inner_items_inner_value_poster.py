# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.tv_series_changes200_response_changes_inner_items_inner_value_poster import TvSeriesChanges200ResponseChangesInnerItemsInnerValuePoster

class TestTvSeriesChanges200ResponseChangesInnerItemsInnerValuePoster(unittest.TestCase):
    """TvSeriesChanges200ResponseChangesInnerItemsInnerValuePoster unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesChanges200ResponseChangesInnerItemsInnerValuePoster:
        """Test TvSeriesChanges200ResponseChangesInnerItemsInnerValuePoster
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesChanges200ResponseChangesInnerItemsInnerValuePoster`
        """
        model = TvSeriesChanges200ResponseChangesInnerItemsInnerValuePoster()
        if include_optional:
            return TvSeriesChanges200ResponseChangesInnerItemsInnerValuePoster(
                file_path = '/ouudK6RCNnsbT1CSXrlATXQIQTG.jpg',
                iso_639_1 = 'en'
            )
        else:
            return TvSeriesChanges200ResponseChangesInnerItemsInnerValuePoster(
        )
        """

    def testTvSeriesChanges200ResponseChangesInnerItemsInnerValuePoster(self):
        """Test TvSeriesChanges200ResponseChangesInnerItemsInnerValuePoster"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
