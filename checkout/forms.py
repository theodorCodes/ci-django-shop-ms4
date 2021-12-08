# Customize Django (checkout) Form
from django import forms  # Import forms from Django
from .models import Order  # Import order model


# Create order form class
class OrderForm(forms.ModelForm):
    class Meta:
        # Connect to Order model
        model = Order
        # Fields to render
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    # Overriding init method of the form
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """

        # Call default init method to set this form as default
        super().__init__(*args, **kwargs)
        # Create dictionary with placeholders to show up inside form fields
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        # Set cursor to appear in the full_name field when page loads
        self.fields['full_name'].widget.attrs['autofocus'] = True
        # Iterate through form fields
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    # Set asterix for field required
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                # Set all fields to their placehoders as set in 'placeholders'
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # Set HTML class to use with custom css styling
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'  # see css in checkout.css
            # Remove default form field labels
            self.fields[field].label = False