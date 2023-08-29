from django import forms
from ExamProject.products.models import Product, ProductCategory


class ProductBaseForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=ProductCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailsForm(ProductBaseForm):
    pass


class ProductCreateForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=ProductCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Product
        fields = '__all__'


class ProductEditForm(ProductBaseForm):
    pass


class ProductDeleteForm(ProductBaseForm):
    pass
