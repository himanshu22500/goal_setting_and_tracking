from django.urls import path

from accounts.views.login import login
from accounts.views.logout import logout
from accounts.views.signup import create_user

urlpatterns = [
    path("signup", create_user),
    path("login", login),
    path("logout", logout),
]
