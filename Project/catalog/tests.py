from django.test import TestCase, Client
from django.core.exceptions import ValidationError
from django.urls.exceptions import NoReverseMatch
from django.urls import reverse

from .models import Item, Category


class PageTests(TestCase):
    fixtures = ['item_test_fixture.json']

    def test_item_list(self):
        response = Client().get(reverse('catalog:item_list'))
        self.assertEqual(
            response.status_code, 200, 'Список товаров не работает'
            )

        self.assertIn('items', response.context)
        self.assertIn('title_name', response.context)
        self.assertEqual(len(response.context['items']), 1)

    def test_item_detail(self):
        # Товар с таким pk существует
        positive_response = Client().get(
            reverse('catalog:item_detail', kwargs={'item_id': 1})
            )
        self.assertIn('item', positive_response.context)
        self.assertIn('title_name', positive_response.context)

        # Товар с таким pk не существует
        negative_response = Client().get(
            reverse('catalog:item_detail', kwargs={'item_id': 9999})
            )
        self.assertNotIn('item', negative_response.context)

    def test_item_detail_url_positive(self):
        pk_list = (1, 10, 100, 200)
        fail_msg = 'При позитивном тесте item_detail ожидался код 200'

        for pk in pk_list:
            with self.subTest('Позитивный тест item_detail', pk=pk):
                try:
                    reverse('catalog:item_detail', kwargs={'item_id': pk})
                except NoReverseMatch:
                    raise self.fail(fail_msg)

    def test_item_detail_url_negative(self):
        pk_list = (0, -1, 1.1, '000111', 'Hello', '1 1')
        fail_msg = 'При негативном тесте item_detail ожидался код 404'

        for pk in pk_list:
            with self.subTest('Тест: catalog/<item_id>', pk=pk):
                with self.assertRaises(NoReverseMatch, msg=fail_msg):
                    reverse('catalog:item_detail', kwargs={'item_id': pk})


class DBTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            name='Тестовая категория', slug='cat-test-slug'
            )

    def create_test_item(self, text):
        return Item.objects.create(
            name='Тестовый товар', text=text,
            category=self.category
            )

    def test_text_validator_positive(self):
        test_texts = [
            'ВЕЛИКОЛЕПНО\nПревосходно!', 'Превосходно', 'Роскошно',
            '<p>Роскошно и превосходно.</p>'
            ]
        fail_msg = (
            'Валидатор описания товара неправильно '
            'работает на позитивном тексте'
            )

        for text in test_texts:
            with self.subTest('Позитивный тест валидатора', text=text):
                item = self.create_test_item(text)
                try:
                    item.full_clean()
                except ValidationError:
                    raise self.fail(fail_msg)

    def test_text_validator_negative(self):
        test_texts = [
            'ВеликолепноПревосходно', 'ДаПревосходноДа', 'Превосходное', ''
            ]
        fail_msg = (
            'Валидатор описания товара неправильно'
            'работает на негативном тесте'
            )

        for text in test_texts:
            with self.subTest('Негативный тест валидатора', text=text):
                self.item = self.create_test_item(text)
                with self.assertRaises(ValidationError, msg=fail_msg):
                    self.item.full_clean()
