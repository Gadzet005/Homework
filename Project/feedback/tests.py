from django.test import TestCase, Client
from django.urls import reverse

from .models import Feedback
from .forms import FeedbackForm


class FormTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FeedbackForm()

    def post_form(self, data):
        return Client().post(
            reverse("feedback:feedback"), data=data, follow=True
            )

    def test_context(self):
        must_contains = ["title_name", "form_title", "form"]

        response = Client().get(reverse("feedback:feedback"))
        for elem in must_contains:
            self.assertIn(elem, response.context)

    def test_form_fields(self):
        email = self.form.fields["email"]
        self.assertEqual(email.label, "Почта")
        self.assertEqual(
            email.help_text,
            "Введите вашу почту, чтобы мы могли связаться с вами"
            )

        text = self.form.fields["text"]
        self.assertEqual(text.label, "Текст")
        self.assertEqual(text.help_text, "Введите ваше сообщение")

    def test_create_feedback(self):
        good_form_data = {
            "email": "test@example.com", "text": "Тестовый текст"
            }
        bad_form_data = {
            "email": "not-valid", "text": "Тестовый текст"
            }

        feedback_count = Feedback.objects.count()

        response = self.post_form(good_form_data)
        self.assertRedirects(response, reverse("feedback:feedback"))

        response = self.post_form(bad_form_data)
        self.assertEqual(response.redirect_chain, list())

        self.assertEqual(Feedback.objects.count(), feedback_count + 1)
