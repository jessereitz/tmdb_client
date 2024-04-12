# coding: utf-8

"""
    TMDB API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.person_movie_credits200_response_crew_inner import PersonMovieCredits200ResponseCrewInner

class TestPersonMovieCredits200ResponseCrewInner(unittest.TestCase):
    """PersonMovieCredits200ResponseCrewInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PersonMovieCredits200ResponseCrewInner:
        """Test PersonMovieCredits200ResponseCrewInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PersonMovieCredits200ResponseCrewInner`
        """
        model = PersonMovieCredits200ResponseCrewInner()
        if include_optional:
            return PersonMovieCredits200ResponseCrewInner(
                adult = False,
                backdrop_path = '/tx3uj8GPWf5pzb0gWATJ4bokNHI.jpg',
                genre_ids = [
                    99
                    ],
                id = 87061,
                original_language = 'fr',
                original_title = 'Le Voyage extraordinaire',
                overview = 'An account of the extraordinary life of film pioneer Georges Méliès (1861-1938) and the amazing story of the copy in color of his masterpiece “A Trip to the Moon” (1902), unexpectedly found in Spain and restored thanks to the heroic efforts of a group of true cinema lovers.',
                popularity = 6.007,
                poster_path = '/zHNNT9gfiGsuadR6x38KYOp6ekq.jpg',
                release_date = '2011-12-08',
                title = 'The Extraordinary Voyage',
                video = False,
                vote_average = 7.6,
                vote_count = 47,
                credit_id = '5d818a63d34eb3002c4f8fea',
                department = 'Crew',
                job = 'Thanks'
            )
        else:
            return PersonMovieCredits200ResponseCrewInner(
        )
        """

    def testPersonMovieCredits200ResponseCrewInner(self):
        """Test PersonMovieCredits200ResponseCrewInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
