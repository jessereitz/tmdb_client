# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tv_series_changes200_response_changes_inner_items_inner_value import TvSeriesChanges200ResponseChangesInnerItemsInnerValue

class TestTvSeriesChanges200ResponseChangesInnerItemsInnerValue(unittest.TestCase):
    """TvSeriesChanges200ResponseChangesInnerItemsInnerValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TvSeriesChanges200ResponseChangesInnerItemsInnerValue:
        """Test TvSeriesChanges200ResponseChangesInnerItemsInnerValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TvSeriesChanges200ResponseChangesInnerItemsInnerValue`
        """
        model = TvSeriesChanges200ResponseChangesInnerItemsInnerValue()
        if include_optional:
            return TvSeriesChanges200ResponseChangesInnerItemsInnerValue(
                poster = openapi_client.models.tv_series_changes_200_response_changes_inner_items_inner_value_poster.tv_series_changes_200_response_changes_inner_items_inner_value_poster(
                    file_path = '/ouudK6RCNnsbT1CSXrlATXQIQTG.jpg', 
                    iso_639_1 = 'en', )
            )
        else:
            return TvSeriesChanges200ResponseChangesInnerItemsInnerValue(
        )
        """

    def testTvSeriesChanges200ResponseChangesInnerItemsInnerValue(self):
        """Test TvSeriesChanges200ResponseChangesInnerItemsInnerValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()