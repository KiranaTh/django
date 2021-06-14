from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .forms import SubscriberForm
from .models import Profile, Email
from .serializers import SubscriberSerializer

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

class SubscriberAPIView(APIView):
    def get(self, request):
        # subscriber = Email.objects.first()
        # serializer = SubscriberSerializer(subscriber)
        subscriber = Email.objects.all()
        serializer = SubscriberSerializer(subscriber, many=True)

        return Response(serializer.data)
        # data = {
        #     "text": "Hello Subscriber"
        # }
        # return JsonResponse(data)

    def post(self, request):
       serializer = SubscriberSerializer(data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 