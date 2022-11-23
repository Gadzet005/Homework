from django.views.generic import CreateView
from django.urls.base import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings

from .forms import FeedbackForm
from .models import Feedback


class CreateFeedback(CreateView):
    template_name = "base_form.html"
    form_class = FeedbackForm
    model = Feedback
    success_url = reverse_lazy("homepage:home")
    extra_context = {
        "title_name": "Обратная связь",
        "button_text": "Отправить",
        "form_title": "Обратная связь",
        "form_description":
        "Вы можете отправить нам сообщение. Возможно мы ответим...",
    }

    def form_valid(self, form):
        send_mail(
            "Заголовок письма", form.cleaned_data["text"],
            settings.OWNER_EMAIL, [form.cleaned_data["email"]],
            fail_silently=True
            )

        return super().form_valid(form)
