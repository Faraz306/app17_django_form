from django.shortcuts import render
from .forms import AppliactionForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

def index(request):
    if request.method == "POST":
        form = AppliactionForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']
            print(first_name, last_name, email, date, occupation)

            Form.objects.create(first_name=first_name, last_name=last_name, email=email, date=date, occupation=occupation)

            message_body = (f"Thank you for your submission at Yamaan Faraz(YF trademark) job form, details:\n"
                            f"first name: {first_name} \n"
                            f" last name: {last_name} \n"
                            f" email: {email} \n"
                            f" date: {date} \n"
                            f" occupation: {occupation}.\n"
                            f"We really appreciate for your submission at Yamaan Faraz(YF trademark).\n"
                            f"From Yamaan Faraz(YF) \n"
                            f"To {first_name}.\n")

            email_message = EmailMessage("Form Submission Successful", message_body, to=[email])
            email_message.send()

            messages.success(request, f'{first_name} {last_name}, Your Data was submitted successfully!')

    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request, 'contact.html')