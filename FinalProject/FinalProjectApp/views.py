from django.shortcuts import render
from .forms import SkillsForm
from .models import Skills


def Home(request):
    return render(request, 'home.html')

def Experience(request):
   return render(request,'experience.html')

def Certifications(request):
    return render(request,'certifications.html')

def Skill(request):
   return render(request,'skills.html')

def ListSkills(request):
    return render(request, 'ListSkills.html')

def About(request):
    return render(request,'about.html')

def addskill(request):
    if request.method == "POST":
        skillform = SkillsForm(request.POST['Description'], request.POST['Level'])
        print(skillform)
        if skillform.is_valid():
            skillinfo = skillform.cleaned_data
            skillinfo = Skills(Description=skillinfo['Description'], Level=skillinfo['Level'])
            skillinfo.save()
            return render(request,'ListSkills.html')
    else:
        skillform = SkillsForm()
    return render(request,'skills.html', {'skillform':skillform})
