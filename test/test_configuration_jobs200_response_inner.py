# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.configuration_jobs200_response_inner import ConfigurationJobs200ResponseInner

class TestConfigurationJobs200ResponseInner(unittest.TestCase):
    """ConfigurationJobs200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigurationJobs200ResponseInner:
        """Test ConfigurationJobs200ResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigurationJobs200ResponseInner`
        """
        model = ConfigurationJobs200ResponseInner()
        if include_optional:
            return ConfigurationJobs200ResponseInner(
                department = 'Production',
                jobs = [
                    'Casting'
                    ]
            )
        else:
            return ConfigurationJobs200ResponseInner(
        )
        """

    def testConfigurationJobs200ResponseInner(self):
        """Test ConfigurationJobs200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
