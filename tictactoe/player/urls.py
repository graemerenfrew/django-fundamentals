from django.conf.urls import url
from .views import home

urlpatterns = [
    url(r'home$', home, name="player_home") #Named URLs are good if I end up changing the structure later


]