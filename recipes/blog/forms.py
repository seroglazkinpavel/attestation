from django import forms
from django.core.exceptions import ValidationError


from .models import *


class AddRecipeForm(forms.ModelForm):
    # ingredients = forms.CharField(help_text="Каждый инградиент обязательно вводится в таком порядке:"
    #                                         " название - количество;", widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Выберите категорию'
        self.fields['user'].empty_label = 'Выберите автора'

    class Meta:
        model = Recipe
        fields = ['category', 'title', 'slug', 'description', 'preparation_steps', 'cooking_time', 'user',
                  'image', 'ingredients']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'rows': 10}),
            'preparation_steps': forms.Textarea(attrs={'rows': 10}),
            'ingredients': forms.Textarea(attrs={'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return title


