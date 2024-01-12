from django.urls import path
from .views import *


urlpatterns = [
    path('', home_page, name='home'),
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', user_logout, name='logout'),
    path('create_page/', creat_page, name='create_page'),
    path('all_page/', all_page, name='all_page'),
    path('del_page/<int:page_id>/', del_page, name='del_page'),
    path('edit_page/<int:page_id>/', edit_page, name='edit_page'),
    path('detail_page/<int:page_id>/', detail_page, name='detail_page'),
    path('random_page/', random_page, name='random_page'),
]
