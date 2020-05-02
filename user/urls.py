from django.conf.urls import url
from . import views

app_name = 'user'
urlpatterns = [
    url(r'^$', views.user, name='user'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register_handle/$', views.register_handle, name='register_handle'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login_check/$', views.login_check, name='login_check'),
    url(r'^logout/$', views.logout, name='logout'),
    # 医生登录
    url(r'^login2/$', views.login2, name='login2'),
    url(r'^login2_check/$', views.login2_check, name='login2_check'),
    # 医生登出
    url(r'^log2out/$', views.log2out, name='log2out'),
    # 修改个人信息
    url(r'^user_change/$', views.user_change, name='user_change'),
]
