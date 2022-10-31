from django.test import TestCase, Client
from django.core.exceptions import ValidationError

from .models import Item, Category, Tag


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
                with self.subTest('Тест: catalog/pk', pk=pk):
                    response = Client().get(f'/catalog/{pk}/')
                    msg = f'От /catalog/{pk}/ ожидался код {expected_code}'
                    self.assertEqual(response.status_code, expected_code, msg)


class DBTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            name='Тестовая категория', slug='cat-test-slug'
            )
        cls.tag = Tag.objects.create(name='Тестовый тег', slug='tag-test-slug')

    def create_test_item(self, text):
        item = Item.objects.create(
            name='Тестовый товар', text=text,
            category=self.category
            )
        return item

    def test_text_validator_positive(self):
        test_texts = [
            'ВЕЛИКОЛЕПНО\nПревосходно!', 'Превосходно', 'Роскошно',
            'Роскошно и превосходно.'
            ]

        for text in test_texts:
            with self.subTest('Позитивный тест валидатора', text=text):
                item = self.create_test_item(text)

                # Проверяем, что валидатор не выдает ошибку
                try:
                    item.full_clean()
                except ValidationError:
                    error_msg = f'Валидатор описания товара неправильно ' \
                                f'работает на позитивном тексте: {text}'
                    raise self.fail(error_msg)

    def test_text_validator_negative(self):
        test_texts = [
            'ВЕЛИКОЛЕПНОПревосходно', 'дПревосходнод', 'Роскош', ''
            ]

        for text in test_texts:
            with self.subTest('Негативный тест валидатора', text=text):
                self.item = self.create_test_item(text)

                # Проверяем, что валидатор выдает ошибку
                error_msg = f'Валидатор описания товара неправильно' \
                            f'работает на негативном тексте: {text}'
                with self.assertRaises(ValidationError, msg=error_msg):
                    self.item.full_clean()
