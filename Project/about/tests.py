from django.test import TestCase, Client
from django.urls import reverse


class PageTests(TestCase):
    def test_description(self):
        response = Client().get(reverse('about:about'))
        self.assertEqual(
            response.status_code, 200, 'Страница 'О нас' не работает'
            )
        self.assertIn('title_name', response.context)
