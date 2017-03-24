from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^lander$', views.lander, name = 'lander'),
    url(r'^itemadder$', views.itemadder, name= 'itemadder'),
    url(r'^itemcreator$', views.itemcreator, name = 'itemcreator'),
    url(r'^iteminfo/(?P<id>\d+)$', views.iteminfo, name = "iteminfo"),
    url(r'^deleteitem/(?P<id>\d+)$', views.deleteitem, name = "deleteitem"),
    url(r'^takewish/(?P<id>\d+)$', views.takewish, name = "takewish"),
    url(r'^makewish/(?P<id>\d+)$', views.makewish, name = "makewish"),
    url(r'^logout$', views.logout, name = "logout")
]
