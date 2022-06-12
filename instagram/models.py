# from django.core.mail import send_mail
# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.conf import settings
# from django.template.loader import render_to_string
#
#
# class User(AbstractUser):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     website_url = models.URLField(blank=True)
#     bio = models.TextField(blank=True)
#
#     def send_welcome_email(self):
#         subject = render_to_string("welcome_email_subject.txt", {"user": self,})
#         content = render_to_string("welcome_email_content.txt", {"user": self,})
#         sender_email = settings.WELCOME_EMAIL_SENDER
#         send_mail(subject, content, sender_email, [self.email], fail_silently=False)
#
#     class Meta:
#         verbose_name_plural = "USER"
#
#
# class Profile(models.Model):
#     pass
