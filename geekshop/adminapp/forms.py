from django import forms
from authapp.models import UserShop
from authapp.forms import UserShopEditForm
from mainapp.models import ProductCategory


class UserShopAdminEditForm(UserShopEditForm):
    class Meta:
        model = UserShop
        fields = '__all__'


class ProductCategoryEditForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
