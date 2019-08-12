from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.conf import settings
from django.http import HttpResponse
from django.template import loader, RequestContext

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import os
import logging

from .models import *

from .forms import *

logger = logging.getLogger(__name__)

def index(request):
    contact_form = ContactForm
    portfolio_section = PortfolioSection.objects.all()[:6]

    header_section = HeaderSection.objects.filter(pk=1).values('master_heading', 'sub_heading')[0]
    about_section = AboutSection.objects.filter(pk=1).values()[0]
    master_heading =  header_section['master_heading']
    sub_heading =  header_section['sub_heading']
    programming_language_list = about_section['programming_language'].split(',')
    database_management_list = about_section['database_management'].split(',')
    markup_and_styling_language_list = about_section['markup_and_styling_language'].split(',')
    framework_list = about_section['framework'].split(',')

    return render(request, 'index.html', 
                {'contact_form': contact_form, 'portfolio_section': portfolio_section, 'master_heading': master_heading, 'sub_heading': sub_heading,
                 'programming_language_list': programming_language_list, 'database_management_list': database_management_list, 
                 'markup_and_styling_language_list': markup_and_styling_language_list, 'framework_list': framework_list})

def send_message(request):
    if request.method == 'POST':
        try:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                name = request.POST['name']
                email = request.POST['email']
                message = request.POST['message']

                content = 'Name: %s\nEmail: %s\nMessage: %s' % (name, email, message)
                message = Mail(
                    from_email='contact.alpolinar@shaw.ca',
                    to_emails='alpolinar@gmail.com',
                    subject="New message from portfolio site.", 
                    html_content=content)
                try:
                    sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
                    response = sg.send(message)
                    return HttpResponse(response.status_code)
                except Exception as e:
                    logger.error('sg: %s', e)
                return HttpResponse('sent')
            else:
                return HttpResponse('not valid')
        except Exception as e:
            logger.error('error: %s', str(e))
    else:
        return HttpResponse('test')
    return HttpResponse('default')

def handler404(request, *args, **argv):
    response = render(request, '404.html')
    response.status_code = 404
    return response

def handler500(request, *args, **argv):
    response = render(request, '500.html')
    response.status_code = 500
    return response