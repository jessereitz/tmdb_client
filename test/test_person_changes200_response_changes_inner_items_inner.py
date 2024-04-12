# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.person_changes200_response_changes_inner_items_inner import PersonChanges200ResponseChangesInnerItemsInner

class TestPersonChanges200ResponseChangesInnerItemsInner(unittest.TestCase):
    """PersonChanges200ResponseChangesInnerItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PersonChanges200ResponseChangesInnerItemsInner:
        """Test PersonChanges200ResponseChangesInnerItemsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PersonChanges200ResponseChangesInnerItemsInner`
        """
        model = PersonChanges200ResponseChangesInnerItemsInner()
        if include_optional:
            return PersonChanges200ResponseChangesInnerItemsInner(
                id = '640469b113654500ba4e859a',
                action = 'added',
                time = '2023-03-05 10:06:41 UTC',
                iso_639_1 = 'ca',
                iso_3166_1 = 'ES',
                value = 'Thomas "Tom" Jeffrey Hanks (Concord, Califòrnia, 9 de juliol de 1956) és un actor de cinema i productor estatunidenc, guanyador dues vegades de l'Oscar al millor actor i considerat un dels més versàtils i talentosos del cinema actual.

Hanks és l'actor que més diners ha guanyat de tota la història del cinema amb un total de gairebé sis mil milions de dòlars (setembre 2006). És també copropietari de Playtone, una companyia de producció de pel·lícules.'
            )
        else:
            return PersonChanges200ResponseChangesInnerItemsInner(
        )
        """

    def testPersonChanges200ResponseChangesInnerItemsInner(self):
        """Test PersonChanges200ResponseChangesInnerItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()