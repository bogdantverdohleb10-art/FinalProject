from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']


class SearchForm(forms.Form):
    STATE_CHOICES = [
        ('', 'Всі штати'),
        ('CA', 'California'),
        ('NY', 'New York'),
        ('TX', 'Texas'),
        ('FL', 'Florida'),
        ('WA', 'Washington')
    ]
    ROOM_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4+')
    ]
    SQFT_CHOICES = [
        ('500', 'До 500 кв. футів'),
        ('1000', '500 - 1000 кв. футів'),
        ('1500', '1000 - 1500 кв. футів'),
        ('2000', 'Більше 1500 кв. футів')
    ]
    PHOTO_CHOICES = [
        ('Yes', 'Є фото'),
        ('No', 'Без фото')
    ]
    PRICE_TYPE_CHOICES = [
        ('Monthly', 'Щомісяця'),
        ('Weekly', 'Щотижня')
    ]
    price_type = forms.ChoiceField(choices=PRICE_TYPE_CHOICES, required=False, label='Періодичність оплати',
                                   widget=forms.Select(attrs={'class': 'form-select'}))

    state = forms.ChoiceField(choices=STATE_CHOICES, required=False, label='Штат',
                              widget=forms.Select(attrs={'class': 'form-select'}))
    bedrooms = forms.ChoiceField(choices=ROOM_CHOICES, required=False, label='Спальні',
                                 widget=forms.Select(attrs={'class': 'form-select'}))
    bathrooms = forms.ChoiceField(choices=ROOM_CHOICES, required=False, label='Ванні кімнати',
                                  widget=forms.Select(attrs={'class': 'form-select'}))
    square_feet = forms.ChoiceField(choices=SQFT_CHOICES, required=False, label='Площа',
                                    widget=forms.Select(attrs={'class': 'form-select'}))
    has_photo = forms.ChoiceField(choices=PHOTO_CHOICES, required=False, label='Наявність фото',
                                  widget=forms.Select(attrs={'class': 'form-select'}))
    latitude = forms.FloatField(required=False, label='Широта', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Наприклад, 38.5'}))
    longitude = forms.FloatField(required=False, label='Довгота', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Наприклад, -77.2'}))