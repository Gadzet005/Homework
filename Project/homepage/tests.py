from django.test import TestCase, Client


class URLTests(TestCase):
    def test_homepage(self):
        response = Client().get('/')
        self.assertEqual(
            response.status_code, 200, 'Главная страница не работает'
            )
