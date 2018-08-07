from django.conf.urls import url
from django.contrib.auth.view import LoginView, LogoutView

from .views import game_detail

urlpatterns=[
    url(r'detail/(?P<id>\d+)/$',
        game_detail,
        name="game_detail")
]