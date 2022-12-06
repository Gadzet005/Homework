from django import forms

from rating.models import ItemRating


class ItemRatingForm(forms.ModelForm):
    class Meta:
        model = ItemRating
        fields = ('rating',)
