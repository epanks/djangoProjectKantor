from django import forms
from .models import Satker, Balai, Paket


class SatkerCreateForm(forms.ModelForm):
    class Meta:
        model = Satker
        fields = ['kdsatker', 'nmsatker', 'phone', 'balai', 'wilayah']


class PaketCreateForm(forms.ModelForm):
    class Meta:
        model = Paket
        fields = ['nmpaket', 'balai', 'wilayah']