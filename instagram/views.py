from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model

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


def user_page(request, username):
    page_user = get_object_or_404(get_user_model(), username=username, is_active=True)
    post_list = Post.objects.filter(author=page_user)
    post_list_count = post_list.count()  # 실제 데이터베이스 count 쿼리 호출
    context = {
        "page_user": page_user,
        "post_list": post_list,
        "post_list_count": post_list_count,
    }
    return render(request, "instagram/user_page.html", context)
