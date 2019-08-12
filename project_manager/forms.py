from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'id': 'name','class': 'form-control', 'type': 'text', 'placeholder': 'Name', 'required': 'required', 'data-validation-required-message': 'Please enter your name.'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'id': 'email','class': 'form-control', 'type': 'email', 'placeholder': 'Email Address', 'required': 'required', 'data-validation-required-message': 'Please enter your email address.'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'id': 'message','class': 'form-control', 'rows': '5', 'placeholder': 'Message', 'required': 'required', 'data-validation-required-message': 'Please enter a message.'}))
    
    def __init__(self, *args, **kwargs):
        return super(ContactForm, self).__init__(*args, *kwargs)
    
    def clean(self):
        return self.cleaned_data
