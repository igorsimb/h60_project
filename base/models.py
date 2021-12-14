from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    pass

# Делаем валидаторы, как советует документация
def validate_title(value):
    if value == "тест":
        raise ValidationError(_('Ну нельзя же "тест" писать!'))

def validate_actor(value):
    if "шмактер" in value:
        raise ValidationError(_('Актер-шмактер! Таких не бывает!'))

class Movie(models.Model):
    title = models.CharField(max_length=50, help_text='Не пишите одно слово тест',
                             verbose_name='Название Фильма',
                             validators=[validate_title])

    actor = models.CharField(max_length=255, verbose_name='Актер в главной роли', help_text='Чтобы никаких шмактеров!',
                             validators=[validate_actor])

    release_year = models.IntegerField(help_text='Между 1900 и 2021', validators=
                                       [MinValueValidator(1900, message='Год должен быть 1900 или больше'),
                                        MaxValueValidator(2021, message='Год должен быть 2021 или меньше')],
                                       verbose_name='Год Релиза')

    def __str__(self):
        return f'{{ self.title}} ({{self.release_year}})'

