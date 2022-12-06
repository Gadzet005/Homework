from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.views.generic import FormView

from rating.forms import ItemRatingForm
from rating.models import ItemRating


class CreateItemRating(LoginRequiredMixin, FormView):
    form_class = ItemRatingForm
    template_name = 'base_form.html'
    extra_context = {
        "title_name": "Оценить",
        "button_text": "Оценить",
        "form_title": "Оценка товара",
    }

    def get_initial(self):
        self.rating = ItemRating.objects.filter(
            user=self.request.user, item_id=self.kwargs['item_id']
            ).first()
        if self.rating:
            self.initial = {'rating': self.rating.rating}
        return super().get_initial()

    def form_valid(self, form):
        if self.rating is None:
            # Создаем оценку
            self.object = form.save(commit=False)
            self.object.item_id = self.kwargs['item_id']
            self.object.user_id = self.request.user.id
            self.object.save()
        else:
            # Изменяем оценку
            self.rating.rating = form.cleaned_data['rating']
            self.rating.save()
        return super().form_valid(form)

    def get_success_url(self):
        self.success_url = reverse_lazy(
            'catalog:item_detail', kwargs={'item_id': self.kwargs['item_id']}
            )
        return super().get_success_url()
