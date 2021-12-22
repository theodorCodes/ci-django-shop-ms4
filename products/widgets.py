# Import from Django widgets
from django.forms.widgets import ClearableFileInput
# Import gettext_lazy as underscore for translation
# to keep custom class close to original classes
# "as _" means option to call gettext_lazy() using _().
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    Create new class that inheritates from Django widgets ClearableFileInput
    """
    # Overriding clear checkbox label
    clear_checkbox_label = _('Remove')
    # Initial text
    initial_text = _('Current Image')
    # Input text
    input_text = _('')
    # Declare template
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'
