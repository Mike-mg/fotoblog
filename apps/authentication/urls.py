from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView,\
    PasswordChangeView, PasswordChangeDoneView


urlpatterns = [
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True,
        next_page='home'),
        name='login'),

    path('logout/',
         LogoutView.as_view(next_page='login'),
         name='logout'),

    path('password_change/', PasswordChangeView.as_view(
        template_name='authentication/password_change.html'),
        name='password_change'),

    path('password_change_done/',
         PasswordChangeDoneView.as_view(
            template_name='authentication/password_change_done.html'),
         name='password_change_done')
]
