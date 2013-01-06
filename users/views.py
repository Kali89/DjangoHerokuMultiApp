from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from users.models import User, Post

def index(request):
    latest_user_list = User.objects.order_by('username')[:5]
    context = {'latest_user_list': latest_user_list}
    return render(request, 'users/index.html', context)

def detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    post_list = Post.objects.filter(id__lt = user.id)  
    return render(request, 'users/detail.html', {'user': user, 'post_list': post_list})


