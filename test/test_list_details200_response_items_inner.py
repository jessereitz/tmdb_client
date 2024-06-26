# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tmdb_client.models.list_details200_response_items_inner import ListDetails200ResponseItemsInner

class TestListDetails200ResponseItemsInner(unittest.TestCase):
    """ListDetails200ResponseItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListDetails200ResponseItemsInner:
        """Test ListDetails200ResponseItemsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListDetails200ResponseItemsInner`
        """
        model = ListDetails200ResponseItemsInner()
        if include_optional:
            return ListDetails200ResponseItemsInner(
                adult = False,
                backdrop_path = '/14QbnygCuTO0vl7CAFmPf1fgZfV.jpg',
                genre_ids = [
                    28
                    ],
                id = 634649,
                media_type = 'movie',
                original_language = 'en',
                original_title = 'Spider-Man: No Way Home',
                overview = 'Peter Parker ist demaskiert und kann sein normales Leben nicht mehr von den hohen Einsätzen als Superheld trennen. Als er Doctor Strange um Hilfe bittet, wird die Lage noch gefährlicher und er muss entdecken, was es wirklich bedeutet, Spider-Man zu sein.',
                popularity = 398.217,
                poster_path = '/iNKf4D0AzOj9GLq8ZyG3WZaqibL.jpg',
                release_date = '2021-12-15',
                title = 'Spider-Man: No Way Home',
                video = False,
                vote_average = 8,
                vote_count = 17267
            )
        else:
            return ListDetails200ResponseItemsInner(
        )
        """

    def testListDetails200ResponseItemsInner(self):
        """Test ListDetails200ResponseItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
