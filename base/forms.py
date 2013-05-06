from django import forms

from .models import Equipo


class SolicitarMembresiaForm(forms.Form):
    equipo = forms.ModelChoiceField(queryset=Equipo.objects.all())
