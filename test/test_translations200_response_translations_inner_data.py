# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.translations200_response_translations_inner_data import Translations200ResponseTranslationsInnerData

class TestTranslations200ResponseTranslationsInnerData(unittest.TestCase):
    """Translations200ResponseTranslationsInnerData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Translations200ResponseTranslationsInnerData:
        """Test Translations200ResponseTranslationsInnerData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Translations200ResponseTranslationsInnerData`
        """
        model = Translations200ResponseTranslationsInnerData()
        if include_optional:
            return Translations200ResponseTranslationsInnerData(
                biography = 'Thomas Jeffrey Hanks (born July 9, 1956) is an American actor and filmmaker. Known for both his comedic and dramatic roles, Hanks is one of the most popular and recognizable film stars worldwide, and is widely regarded as an American cultural icon.

Hanks made his breakthrough with leading roles in the comedies Splash (1984) and Big (1988). He won two consecutive Academy Awards for Best Actor for starring as a gay lawyer suffering from AIDS in Philadelphia (1993) and a young man with below-average IQ in Forrest Gump (1994). Hanks collaborated with film director Steven Spielberg on five films: Saving Private Ryan (1998), Catch Me If You Can (2002), The Terminal (2004), Bridge of Spies (2015), and The Post (2017), as well as the 2001 miniseries Band of Brothers, which launched him as a director, producer, and screenwriter.

Hanks' other notable films include the romantic comedies Sleepless in Seattle (1993) and You've Got Mail (1998); the dramas Apollo 13 (1995), The Green Mile (1999), Cast Away (2000), Road to Perdition (2002), and Cloud Atlas (2012); and the biographical dramas Saving Mr. Banks (2013), Captain Phillips (2013), Sully (2016), and A Beautiful Day in the Neighborhood (2019). He has also appeared as the title character in the Robert Langdon film series, and has voiced Sheriff Woody in the Toy Story film series.

Description above from the Wikipedia article Tom Hanks, licensed under CC-BY-SA, full list of contributors on Wikipedia.'
            )
        else:
            return Translations200ResponseTranslationsInnerData(
        )
        """

    def testTranslations200ResponseTranslationsInnerData(self):
        """Test Translations200ResponseTranslationsInnerData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
