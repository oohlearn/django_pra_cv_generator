from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io 
# Create your views here.


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        summary = request.POST.get("summary")
        skills = request.POST.get("skills")
        degree = request.POST.get("degree")
        school = request.POST.get("school")
        previous_work = request.POST.get("previous_work")
        portfolio = request.POST.get("portfolio")

        profile = Profile(name=name, email=email, phone=phone,
                          skills=skills, degree=degree, school=school,
                          previous_work=previous_work, portfolio=portfolio,
                          summary=summary)

        profile.save()

    return render(request, 'pdf/accept.html')


def resume(request, id):
    user_profile = Profile.objects.get(id=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({"user_profile": user_profile})
    
    options = {
        "page-size": "letter",
        "encoding": "utf-8",
    }
    pdf = pdfkit.from_string(html, False, options=options)
    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename=resume.pdf"
                            
    return response


def profile_list(request):
    resume_list = Profile.objects.all()
    return render(request, 'pdf/profile_list.html', {
        'resume_list': resume_list})
