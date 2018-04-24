from django.contrib.auth.views import login ,logout
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path("login", login, {'template_name': 'accounts/login.html'}, name="login"),
    path("logout", logout, {'next_page': '/'}, name="logout"),
]