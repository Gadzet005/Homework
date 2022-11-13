from django.test import TestCase, Client
from django.urls import reverse


class PageTests(TestCase):
    def test_homepage(self):
        response = Client().get(reverse('homepage:home'))
        self.assertEqual(
            response.status_code, 200, 'Главная страница не работает'
            )
        self.assertIn('title_name', response.context)
