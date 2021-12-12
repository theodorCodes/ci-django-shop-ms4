from django import forms  # Import Django forms
from .models import UserProfile  # Import profile from model

# Import this form in views.py
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile  # Model name in metaclass
        exclude = ('user',)  # Exclude user field as it shouldn't be changable

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        # Get available fields from models.py
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        # Set autofocus on phone number
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            # Set country as defaut_country
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # Set class to use for CSS styling, see css
            self.fields[field].widget.attrs['class'] = 'profile-style-input'
            self.fields[field].label = False