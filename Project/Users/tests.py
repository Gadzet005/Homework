import datetime

from django.test import TestCase, Client

from Users.models import User


class ContextProcessorTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_exist(self):
        now = datetime.date.today()
        users = User.objects.filter(
            birthday_date__month=now.month,
            birthday_date__day=now.day,
        )
        response = Client().get('/')
        self.assertEqual(
            response.status_code, 200, 'Главная страница не работает'
            )
        self.assertIn('users_with_birthday', response.context)
        self.assertEqual(
            len(response.context['users_with_birthday']),
            len(users)
        )

        for elem in users:
            self.assertIn(elem, response.context['users_with_birthday'])
