from django.test import TestCase, Client


class URLTests(TestCase):
    def test_item_list(self):
        response = Client().get('/catalog/')
        self.assertEqual(
            response.status_code, 200, 'Каталог не работает'
            )

    def test_item_detail(self):
        def test_item_pk(pk, expected_code):
            response = Client().get(f'/catalog/{pk}/')
            with self.subTest(
                    'Элемент каталога вернул неправильный статус', pk=pk
                    ):
                self.assertEqual(response.status_code, expected_code)

        # Тестовые случаи
        pk_tests = {
            200: (1, 12, 100),
            404: (0, -1, 1.1, '000111', 'Hello', '1 1')
        }

        for expected_code, pk_list in pk_tests.items():
            for pk in pk_list:
                test_item_pk(pk, expected_code)
