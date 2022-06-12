from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import SignupForm, SigninForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login as auth_login


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            auth_login(request, signed_user)
            messages.success(request, "회원가입을 환영합니다.")
            signed_user.send_welcome_email()  # FixedME
            next_url = request.GET.get("next", "instagram:index")
            return redirect(next_url)
    else:
        form = SignupForm()

    context = {"form": form}
    return render(request, "accounts/signup_form.html", context)


class SigninView(LoginView):
    template_name = "accounts/signin_form.html"
    # success_url = reverse_lazy("instagram:index")

    def form_valid(self, form):
        messages.error(self.request, "로그인에 실패하였습니다.", extra_tags="danger")
        return super().form_valid(form)


class SignoutView(LogoutView):
    pass


@login_required
def profile_edit(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "프로필을 수정/저장했습니다.")
            return redirect("accounts:profile_edit")
    else:
        form = ProfileForm(instance=request.user)
    context = {"form": form}
    return render(request, "accounts/profile_edit_form.html", context)
