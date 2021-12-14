from django import forms
from .models import Movie

from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field, Fieldset, ButtonHolder, Submit, HTML, Div, Button



class CreateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

    # Полезная инфа: у этой валидации приоритет над валидацией на уровне Модели
    # Закомментировал, т.к. оно почему-то не дружит с crispy_bootstrap5, полагаю, потому что мы вынуждены HTML
    # пропивать здесь, а не в самом шаблоне

    # def clean_release_year(self):
    #     release_year = self.cleaned_data['release_year']
    #     if release_year < 1900:
    #         self.add_error('release_year', '>= 1900!')
    #     if release_year > 2021:
    #         self.add_error('release_year', '<= 2021!')
    #     return self.cleaned_data['release_year']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(

                FloatingField('title'),
                FloatingField('actor'),
                FloatingField('release_year'),
            HTML('<button type="submit" class="btn btn-outline-info">Добавить</button>'),
            )

