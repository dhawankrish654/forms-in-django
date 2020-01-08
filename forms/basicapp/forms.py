from django import forms
from basicapp.models import user


class NewUserForm(forms.ModelForm):

    class Meta:
        model=user
        fields='__all__'
