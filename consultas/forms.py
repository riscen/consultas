from django import forms
from .models import Edificio, Aula, Semestre
from django.contrib.auth.models import User

class SelectEdificioForm(forms.Form):
    edificio = forms.ModelChoiceField(
        label='Edificios',
        queryset=Edificio.objects.all(),
        empty_label='No especificado'
    )
    aula = forms.ModelChoiceField(
        queryset=Aula.objects.all(),
        empty_label=None
    )
    calendario = forms.ModelChoiceField(
        queryset=Semestre.objects.none(),
        empty_label=None
    )

    def __init__(self, *args, **kwargs):
        super(SelectEdificioForm, self).__init__(*args, **kwargs)
        self.fields['aula'].queryset = Aula.objects.none()

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']