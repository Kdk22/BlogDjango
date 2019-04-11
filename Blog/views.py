from django.shortcuts import render
from django.http import HttpResponse
from .models import User,Posts , Comment
# Create your views here.


def index(request):
    all_posts = Posts.objects.all()
    return render(request, 'blog/index.html', {'all_users': all_posts})


def user_info(request , user_id):
    all_user = User.objects.all()
    return render(request, 'blog/user_info.html', {'all_user':all_user})
