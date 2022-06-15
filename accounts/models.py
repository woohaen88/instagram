from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.shortcuts import resolve_url
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    follower_set = models.ManyToManyField("self", blank=True)
    following_set = models.ManyToManyField("self", blank=True)
    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(
        blank=True,
        upload_to="accounts/avatar//%Y/%m/%d",
        help_text="20px * 20px 크기의 파일을 업로드해주세요",
    )
    phone_number = models.CharField(
        max_length=13,
        validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")],
        blank=True,
        help_text="전화번호를 입력하세요",
    )

    class GenderChoices(models.TextChoices):
        MALE = "M", _("Male")
        FEMAIL = "F", _("Female")

    gender = models.CharField(max_length=1, choices=GenderChoices.choices, blank=True)

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        else:
            return resolve_url("pydenticon_image", self.username)

    def send_welcome_email(self):
        subject = render_to_string("welcome_email_subject.txt", {"user": self,})
        content = render_to_string("welcome_email_content.txt", {"user": self,})
        sender_email = settings.WELCOME_EMAIL_SENDER
        send_mail(subject, content, sender_email, [self.email], fail_silently=False)

    class Meta:
        verbose_name_plural = "USER"


class Profile(models.Model):
    pass
