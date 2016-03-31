from django import forms
from django.forms import ModelForm
from market.models import Service
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=20)
    last_name = forms.CharField(required=True, max_length=20)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class ServiceForm(ModelForm):
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea)
    starting_bid = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=True
    )
    final_time = forms.CharField(max_length=20, required=True)

    class Meta:
        model = Service
        fields = ('title', 'description', 'starting_bid', 'final_time')
