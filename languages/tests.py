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


    def tearDown(self):
        self.factory = None


    def test_create_language(self):
        request = self.factory.post('/programming-languages/', emerald,
                                    format='json')
        response = LanguageDetail.as_view()(request)
        self.assertEquals(response.status_code, 201)
        self.assertEquals(Language.objects.filter(slug='emerald').count(), 1)
        self.assertEquals(Language.objects.filter( \
                          slug='emerald').first().is_visible, False)
        # test API response with new language
        get_lang = self.factory.get('/programming-languages/emerald')
        response_lang = LanguageDetail.as_view()(get_lang, slug='emerald')
        # not approved, so should not be found, API returns 404
        self.assertEquals(response_lang.status_code, 404)

