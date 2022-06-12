from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True
        self.fields["first_name"].required = False
        self.fields["last_name"].required = False

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "email", "first_name", "last_name"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email:
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError("이미 등록된 이메일 주소입니다.")
        return email


class SigninForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "avatar",
            "first_name",
            "last_name",
            "website_url",
            "bio",
            "phone_number",
            "gender",
        ]
