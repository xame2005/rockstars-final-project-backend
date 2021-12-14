from django.shortcuts import render, reverse
from django.views import generic
from .forms import ContactForm
from django.core.mail import send_mail
from rockstars_marketplace import settings
from django.contrib import messages

# Create your views here.


class Homeview(generic.TemplateView):
    template_name = 'index.html'


class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse('contact')

    def form_valid(self, form):
        messages.info(self.request, 'Thank you for your message.')
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')

        full_message = f"""
        Received message from {name} ({email}):
        _______________________________________

        
        {message}
        """
        send_mail(
            subject='Message from Contact Form',
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
        )

        return super(ContactView, self).form_valid(form)
