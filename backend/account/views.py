import os

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import LoginForm, UserRegistrationForm, UploadFileForm
from .models import PDFUpload
import PyPDF2


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html',
                  {'section': 'dashboard'})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Authentication succeed.')
            else:
                return HttpResponse('Account is blocked.')
        else:
            return HttpResponse('Wrong authentication data.')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # make new user object without saving in db
            new_user = user_form.save(commit=False)
            # Set new password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save user object
            new_user.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})

    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'upload_success.html', {'file_name': form.title})
        else:
            form = UploadFileForm()
        return render(request, "dashboard.html", {'form': form})


pdf_path = PDFUpload.file


def pdf_to_text(pdf_path, output_txt):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    with open(output_txt, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)


if __name__ == "__main__":
    output_txt = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'files')
    pdf_to_text(pdf_path, output_txt)
