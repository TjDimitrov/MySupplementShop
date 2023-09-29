from django import forms
from ExamProject.products.models import Product, ProductCategory, Review


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


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment_text']
        widgets = {
            'comment_text': forms.Textarea(
                attrs={'placeholder': 'Add comment...'}
            )
        }
