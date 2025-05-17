from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from blog.models import Post  # Импортируем модель постов
from .forms import UserEditForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def profile(request, username):
    # Получаем пользователя или возвращаем 404
    profile_user = get_object_or_404(User, username=username)

    # Получаем посты пользователя с пагинацией
    posts = Post.objects.filter(author=profile_user).order_by('-pub_date')
    paginator = Paginator(posts, 10)  # 10 постов на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/profile.html', {
        'profile': profile_user,
        'page_obj': page_obj,
    })


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('blog:profile', username=request.user.username)
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'blog/user.html', {'form': form})
