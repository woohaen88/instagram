from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from instagram.forms import PostForm
from django.contrib import messages

from .models import Tag, Post


def index(request):
    return render(request, "index.html")


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            post.tag_set.add(*post.extract_tag_list())
            messages.success(request, "포스팅을 저장했습니다.")
            return redirect(post)  # TODO get absolute_url 활용
    else:
        form = PostForm()

    context = {"form": form}
    return render(request, "instagram/post_form.html", context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {"post": post}
    return render(request, "instagram/post_detail.html", context)
