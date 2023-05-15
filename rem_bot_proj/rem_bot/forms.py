from django import forms
from .models import Profile,Stat

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
            'external_id',
            'name',
            'username',
            'count',
        )
        widgets = {
            'name': forms.TextInput
        }
class StatForm(forms.ModelForm):

    class Meta:
        model = Stat
        fields = (
            'date',
            'count',

        )
        widgets = {
            'count': forms.TextInput
        }