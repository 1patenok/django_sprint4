from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('profile/<slug:username>/', user_views.profile, name='profile'),
    path('profile/edit/', user_views.edit_profile, name='edit_profile'),

    path('password_change/',
         auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'
    ),
]
