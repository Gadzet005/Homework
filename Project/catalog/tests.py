from django.test import TestCase, Client


class URLTests(TestCase):
    def test_item_list(self):
        response = Client().get('/catalog/')
        self.assertEqual(
            response.status_code, 200, 'Каталог не работает'
            )

    def test_item_detail(self):
        # Тестовые случаи
        pk_tests = {
            200: (1, 12, 100),
            404: (0, -1, 1.1, '000111', 'Hello', '1 1')
        }

        for expected_code, pk_list in pk_tests.items():
            for pk in pk_list:
                with self.subTest('Тест сatalog pk', pk=pk):
                    response = Client().get(f'/catalog/{pk}/')
                    self.assertEqual(response.status_code, expected_code)
