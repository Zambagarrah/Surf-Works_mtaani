from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import EmployerRegistrationForm, EmployeeRegistrationForm, DocumentUploadForm
from .models import CustomUser, Document
from django.forms import modelformset_factory

# 👥 Step 1: Role selection view
def register_choice(request):
    return render(request, 'users/register_choice.html')

# 📎 Document handler called after user is saved
def handle_documents(request, user):
    DocumentFormSet = modelformset_factory(Document, form=DocumentUploadForm, extra=2)

    if request.method == 'POST':
        formset = DocumentFormSet(request.POST, request.FILES, queryset=Document.objects.none())
        if formset.is_valid():
            for form in formset:
                doc = form.save(commit=False)
                doc.user = user
                doc.save()
            return True
    return False

# 🧑 Employer registration with document support
def register_employer(request):
    DocumentFormSet = modelformset_factory(Document, form=DocumentUploadForm, extra=2)

    if request.method == 'POST':
        form = EmployerRegistrationForm(request.POST)
        formset = DocumentFormSet(request.POST, request.FILES, queryset=Document.objects.none())
        if form.is_valid() and formset.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.role = 'EMPLOYER'
            user.save()
            login(request, user)

            for doc_form in formset:
                doc = doc_form.save(commit=False)
                doc.user = user
                doc.save()
            return redirect('employer_dashboard')
    else:
        form = EmployerRegistrationForm()
        formset = DocumentFormSet(queryset=Document.objects.none())
    return render(request, 'users/register_employer.html', {'form': form, 'formset': formset})

# 👷 Employee registration with document support
def register_employee(request):
    DocumentFormSet = modelformset_factory(Document, form=DocumentUploadForm, extra=2)

    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        formset = DocumentFormSet(request.POST, request.FILES, queryset=Document.objects.none())
        if form.is_valid() and formset.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.role = 'EMPLOYEE'
            user.save()
            login(request, user)

            for doc_form in formset:
                doc = doc_form.save(commit=False)
                doc.user = user
                doc.save()
            return redirect('employee_dashboard')
    else:
        form = EmployeeRegistrationForm()
        formset = DocumentFormSet(queryset=Document.objects.none())
    return render(request, 'users/register_employee.html', {'form': form, 'formset': formset})
