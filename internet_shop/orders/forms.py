from django import forms
from shop.models import Order


class OrderCreateForm(forms.Form):
    # Можно добавить поля, если нужно, например: имя, телефон, адрес
    pass