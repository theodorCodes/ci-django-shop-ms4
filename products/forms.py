from django import forms  # Import forms
from .widgets import CustomClearableFileInput  # Import widget with custom classes
from .models import Product, Category  # Import product and category model


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product  # Model
        fields = '__all__'  # Fields to include

    # Replacing image field on form, utilizing widget with custom classes
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    # Overriding init method
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get categories
        categories = Category.objects.all()
        # And create tuple with id and friendly_name from categories
        # using list comprehension
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # Then update category fields with friendly_names as choices
        self.fields['category'].choices = friendly_names
        # Iterate through fields to attach class for CSS styling
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-inner-content'