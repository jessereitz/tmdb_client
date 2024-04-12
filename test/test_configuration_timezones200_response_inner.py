# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.configuration_timezones200_response_inner import ConfigurationTimezones200ResponseInner

class TestConfigurationTimezones200ResponseInner(unittest.TestCase):
    """ConfigurationTimezones200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigurationTimezones200ResponseInner:
        """Test ConfigurationTimezones200ResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigurationTimezones200ResponseInner`
        """
        model = ConfigurationTimezones200ResponseInner()
        if include_optional:
            return ConfigurationTimezones200ResponseInner(
                iso_3166_1 = 'AD',
                zones = [
                    'Europe/Andorra'
                    ]
            )
        else:
            return ConfigurationTimezones200ResponseInner(
        )
        """

    def testConfigurationTimezones200ResponseInner(self):
        """Test ConfigurationTimezones200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()