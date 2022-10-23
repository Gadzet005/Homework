from django.test import TestCase, Client


class URLTests(TestCase):
    def test_description(self):
        response = Client().get('/about/')
        self.assertEqual(
            response.status_code, 200, 'Страница "О нас" не работает'
            )
