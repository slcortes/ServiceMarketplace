from django import forms
from market.models import Service, Review
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin import widgets


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


class ServiceForm(forms.ModelForm):
    final_time = forms.SplitDateTimeField(input_date_formats=['%m/%d/%Y'],
                                          input_time_formats=['%H:%M%p'])

    class Meta:
        model = Service
        fields = (
            'title',
            'description',
            'category',
            'bid',
            'final_time',
            'location'
        )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'rating',
            'account_type',
            'comment',
        )
