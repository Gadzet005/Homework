from django.test import TestCase, Client
from django.urls import reverse

from .models import Feedback
from .forms import FeedbackForm
from Users.models import User


class FormTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(
            email='test@gmail.com', password='test-password', nickname='test'
            )
        cls.client = Client()

    def test_context(self):
        must_contains = ["title_name", "form_title", "form"]

        self.client.login(username='test@gmail.com', password='test-password')

        response = self.client.get(reverse("feedback:feedback"))
        for elem in must_contains:
            self.assertIn(elem, response.context)

    def test_form_fields(self):
        form = FeedbackForm()
        text = form.fields["text"]
        self.assertEqual(text.label, "Текст")
        self.assertEqual(text.help_text, "Введите ваше сообщение")

    def test_create_feedback(self):
        feedback_count = Feedback.objects.count()

        self.client.login(username='test@gmail.com', password='test-password')

        response = self.client.post(
            reverse("feedback:feedback"), data={'text': 'TestText'},
            follow=True
            )
        self.assertRedirects(response, reverse("homepage:home"))

        self.assertEqual(Feedback.objects.count(), feedback_count + 1)
