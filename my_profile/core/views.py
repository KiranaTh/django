from django.shortcuts import render
from django.views import View

from core.forms import SubscriberForm
from core.models import Profile, Email

# Create your views here.


# def index(request):
#     return render(request, 'profile.html')


class IndexView(View):
    def get(self, request):
        profile = Profile.objects.get(id=1)
        name = profile.name
        form = SubscriberForm()
        fullname = profile.fullname
        birthDate = profile.birthDate
        age = profile.age
        education = profile.education
        university = profile.university
        workplace = profile.workplace
        position = profile.position
        pic_url = profile.pic_url
        facebook_url = profile.facebook_url
        instragram_url = profile.instragram_url
        github_url = profile.github_url
        return render(
            request,
            "profile.html",
            {
                "name": name,
                "form": form,
                "fullname": fullname,
                "birthDate": birthDate,
                "age": age,
                "education": education,
                "university": university,
                "workplace": workplace,
                "position": position,
                "pic_url": pic_url,
                "facebook_url": facebook_url,
                "instragram_url": instragram_url,
                "github_url": github_url,
            },
        )

    def post(self, request):
        print(request.POST)
        print(request.POST.get("email"))

        profile = Profile.objects.get(id=1)
        form = SubscriberForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data.get("email"))
            newEmail = form.cleaned_data.get("email")
            Email.objects.create(email=newEmail)

        name = profile.name

        return render(
            request,
            "thank.html",
            {
                "name": name,
            },
        )
