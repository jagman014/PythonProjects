from django import forms
from django.core import validators

def check_for_z(value: str):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Name needs to start with Z')


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter email again')
    text = forms.CharField(widget=forms.Textarea)
    bot_catcher = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        validators=[validators.MaxLengthValidator(0)]
    )

    # default validator
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verify_email = all_clean_data['verify_email']

        if email != verify_email:
            raise forms.ValidationError('Emails don\'t match')

    # Example custom validator
    def clean_bot_catcher(self):
        bot_catcher = self.cleaned_data['bot_catcher']
        
        if len(bot_catcher) > 0:
            raise forms.ValidationError("Bot Detected")
        
        return bot_catcher
