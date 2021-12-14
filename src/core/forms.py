from django import forms


class ContactForm (forms.Form):
    name = forms.CharField(label='Your name', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Your name'}))
    email = forms.EmailField(label='Your email', widget=forms.TextInput(
        attrs={'placeholder': 'Your name'}))
    message = forms.CharField(label='Message', widget=forms.TextInput(
        attrs={'placeholder': 'Your message'}))
