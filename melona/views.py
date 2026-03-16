from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import ContactEnquiry

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')


def contact(request):
    if request.method == "POST":
        first_name = request.POST.get('c_fname')
        last_name = request.POST.get('c_lname')
        email = request.POST.get('c_email')
        phone = request.POST.get('c_phone')
        wedding_date = request.POST.get('c_wedding_date')
        subject = request.POST.get('c_subject')
        message = request.POST.get('c_message')

        ContactEnquiry.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        return render(request, "contact.html", {"success": True})

    return render(request, "contact.html")



from django.http import HttpResponse

def ping(request):
    return HttpResponse("OK")