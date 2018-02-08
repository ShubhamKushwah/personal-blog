from django.conf.urls import url

from .views import delete, HomeView

app_name = 'home'

urlpatterns = [

    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^(?P<pk>\d+)/delete/$', delete, name='delete'),

]