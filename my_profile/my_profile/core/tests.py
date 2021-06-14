# from django.http import response
from django.test import TestCase
from .models import Profile, Email


class TestProfile(TestCase):
    def test_profile_should_have_defined_fields(self):
        profile = Profile.objects.create(
            name="Jill",
            fullname="Kirana Thanasuttiwat",
            birthDate="8 October 1998",
            age="23",
            education="Computer Science",
            university="King Mongkut's University of Technology Thonburi",
            workplace="ODDS",
            position="Software Developer",
            pic_url="https://avatars.githubusercontent.com/u/36392004?v=4",
            facebook_url="https://www.facebook.com/kirana.thanasuttiwat",
            instragram_url="https://www.instagram.com/jillyjunggg/?hl=en",
            github_url="https://github.com/KiranaTh",
        )

        assert profile.name == "Jill"
        assert profile.fullname == "Kirana Thanasuttiwat"
        assert profile.birthDate == "8 October 1998"
        assert profile.age == "23"
        assert profile.education == "Computer Science"
        assert profile.university == "King Mongkut's University of Technology Thonburi"
        assert profile.workplace == "ODDS"
        assert profile.position == "Software Developer"
        assert profile.pic_url == "https://avatars.githubusercontent.com/u/36392004?v=4"
        assert profile.facebook_url == "https://www.facebook.com/kirana.thanasuttiwat"
        assert profile.instragram_url == "https://www.instagram.com/jillyjunggg/?hl=en"
        assert profile.github_url == "https://github.com/KiranaTh"


class TestIndexView(TestCase):
    def text_index_view_should_see_my_name(self):
        # Given
        Profile.objects.create(name="Jill")

        # When
        response = self.client.get("/")

        # Then
        assert response.status_code == 200
        assert "Jill" in str(response.content)

    def test_index_view_should_save_subscriber_email_when_input_form(self):
        # Given
        Profile.objects.create(name="Jill")

        # When
        data = {
            "email": "eskimo.toy@gmail.com"
        }
        response = self.client.post("/", data=data)

        # Then
        email = Email.objects.last()
        assert response.status_code == 200
        assert email.email == "eskimo.toy@gmail.com"


class TestEmail(TestCase):
    def test_email_should_have_defined_fields(self):
        email = Email.objects.create(
            email="eskimo.toy@gmail.com",
        )

        assert email.email == "eskimo.toy@gmail.com"
