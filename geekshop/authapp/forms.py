from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from authapp.models import UserShop


class UserShopLoginForm(AuthenticationForm):
    class Meta:
        model = UserShop
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserShopLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserShopRegisterForm(UserCreationForm):
    class Meta:
        model = UserShop
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super(UserShopRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError('Возраст менее 18 лет')
        return data


class UserShopEditForm(UserChangeForm):
    class Meta:
        model = UserShop
        fields = ('username', 'first_name', 'password', 'email', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super(UserShopEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError('Возраст менее 18 лет')
        return data