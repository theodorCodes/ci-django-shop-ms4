from django import forms  # Import forms
from .widgets import CustomClearableFileInput  # Import widget with custom classes
from .models import Product, Category, Type, Format  # Import product and category model


# Product form for custom and non custom products
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product  # Model
        fields = '__all__'  # Fields to include

    # Replacing image field on form, utilizing widget with custom classes
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    # Overriding init method
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Get specific 'custom_product' category, types and formats
        categories = Category.objects.all()
        types = Type.objects.all()
        formats = Format.objects.all()

        # And create tuple with id and friendly_name from types
        # using list comprehension
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        friendly_type_names = [(c.id, c.get_friendly_name()) for c in types]
        friendly_format_names = [(c.id, c.get_friendly_name()) for c in formats]

        # Then update category fields with friendly_names as choices
        self.fields['category'].choices = friendly_names
        self.fields['type'].choices = friendly_type_names
        self.fields['format'].choices = friendly_format_names

        # Iterate through fields to attach class for CSS styling
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-inner-content'