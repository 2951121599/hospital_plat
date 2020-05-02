from django.conf.urls import url
from . import views

app_name = 'doctor'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user$', views.user, name='user'),
    url(r'^treatment_record$', views.treatment_record, name='treatment_record'),
]
