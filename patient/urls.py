from django.conf.urls import url
from . import views

app_name = 'patient'
urlpatterns = [
    # url(r'^$', views.user, name='user'),
    # http://127.0.0.1:8000/
    url(r'^$', views.index, name='index'),
    # # http://127.0.0.1:8000/index/
    # url(r'^index$', views.index),
    # 在线问诊
    url(r'^online_inquiry/$', views.online_inquiry, name='online_inquiry'),
    # 在线购药
    url(r'^online_shopping/$', views.online_shopping, name='online_shopping'),

    # http://127.0.0.1:8000/doctor/1
    url(r'^doctor/(?P<doctor_id>\d+)$', views.detail, name='detail'),
    # http://127.0.0.1:8000/search
    url(r'^search$', views.search, name='search'),

    # http://127.0.0.1:8000/doctor/inquiry
    url(r'^inquiry$', views.inquiry, name='inquiry'),

    # inquiry_record
    url(r'^inquiry_record$', views.inquiry_record, name='inquiry_record'),
    # shopping_record
    url(r'^shopping_record$', views.shopping_record, name='shopping_record'),

    # 查看回复
    # http://127.0.0.1:8000/doctor/reply/2
    url(r'^reply/(?P<question_id>\d+)$', views.reply, name='reply'),
    # 查找药品
    # http://127.0.0.1:8000/search
    url(r'^search_medicine$', views.search_medicine, name='search_medicine'),
    # 购药
    # http://127.0.0.1:8000/take_medicine
    url(r'^take_medicine$', views.take_medicine, name='take_medicine'),
    # 二维码
    url(r'^erweima$', views.erweima, name='erweima'),
    # 药品详情页
    url(r'^product_details$', views.product_details, name='product_details'),
    # 购物车
    url(r'^cart$', views.cart, name='cart'),
    # 药品列表页product_list
    url(r'^product_list$', views.product_list, name='product_list'),

]
