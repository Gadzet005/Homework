from django.test import TestCase, Client


class URLTests(TestCase):
    def test_item_list(self):
        response = Client().get('/catalog/')
        self.assertEqual(
            response.status_code, 200, 'Каталог не работает'
            )

    def test_item_detail(self):
        positive_pk_list = [1, 12, 100]
        negative_pk_list = [0, -1, 1.1, '000111', 'Hello', "1%201"]

        # Проверяем позитивные тесты
        for test_pk in positive_pk_list:
            response = Client().get(f'/catalog/{test_pk}/')
            self.assertEqual(
                response.status_code, 200,
                f'Страница предмета с pk={test_pk} должна быть найдена'
                )

        # Проверяем негативные тесты
        for test_pk in negative_pk_list:
            response = Client().get(f'/catalog/{test_pk}/')
            self.assertEqual(
                response.status_code, 404,
                f'Страница предмета с pk={test_pk} не должна быть найдена'
                )
