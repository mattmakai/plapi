from django.test import TestCase
from rest_framework.test import APIRequestFactory, APITestCase
from .views import LanguageDetail
from .models import Language


emerald = {'name': 'Emerald', 'summary': 'A combination of Python and Ruby.',
           'homepage_url': 'http://www.fullstackpython.com/'}


class ProgrammingLanguagesTest(APITestCase):
    """
        Ensures the /programming-languages/ endpoint properly retrieves
        and creates programming languages.
    """

    def setUp(self):
        self.factory = APIRequestFactory()

    def test_create_language(self):
        request = self.factory.post('/programming-languages/', emerald,
                                    format='json')
        response = LanguageDetail.as_view()(request)
        self.assertEquals(response.status_code, 201)
        self.assertEquals(1, Language.objects.filter(slug='emerald').count())
