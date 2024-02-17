from django.shortcuts import render, redirect, HttpResponseRedirect
from enroll.models import Student
from enroll.forms import StudentRegistrationForm
from django.contrib import messages

# Create your views here.

def student_registration(request):
    if request.method == 'POST':
        
        fm = StudentRegistrationForm(request.POST)
        
        if fm.is_valid():
            # If 'Save as Draft' button is clicked
            if 'save_draft' in request.POST:
                convocation = fm.save(commit=False)
                convocation.is_draft = True
                # convocation.save()
                return redirect('regi/drafts')  # Redirect to a page showing drafts
        
            elif 'submit' in request.POST:
                convocation = fm.save(commit=False)
                convocation.is_draft = False
                convocation.save()
                return redirect('regi/submit')  # Redirect to a page showing submitted convocations
    else:
        fm = StudentRegistrationForm()
    return render(request, 'enroll/registration.html', {'form': fm})


def draft_convocations_list(request):

    if request.method == 'POST':
        fm = StudentRegistrationForm(request.POST)
        
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Your data is saved')
    else:

        fm = StudentRegistrationForm()
    return render(request, 'enroll/drafts.html', {'form':fm})



def submitted_convocations_list(request):
    sub_list = Student.objects.all()
    return render(request, 'enroll/submitted.html', {'sub_list':sub_list})

