from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('classification/', views.classification, name='classification'),
    path('classification/community/', views.community, name='community'),
    path('classification/for_sale/', views.for_sale, name='for_sale'),
    path('classification/studying/', views.studying, name='studying'),
    path('classification/school/', views.school, name='school'),
    #失物招领
    path('classification/community/lost_find/', views.L_F, name='lost_find'),
    path('classification/community/lost_find/<int:L_F_T_id>/', views.L_F_T, name='lost_find_topic'),
    path('classification/community/lost_find/new_topic/', views.LFT_new_topic, name='LFT_new_topic'),
    path('classification/community/lost_find/new_entry/<int:L_F_T_id>/', views.LFT_new_entry, name='LFT_new_entry'),
    path('classification/community/lost_find_edit_entry/<int:L_F_E_id>/', views.LFT_edit_entry, name='LFT_edit_entry'),
    #电子产品
    path('classification/for_sale/electronics/', views.electronics, name='electronics'),
    path('classification/for_sale/electronics/<int:E_T_id>/', views.E_T, name='electronics_topic'),
    path('classification/for_sale/electronics/new_topic/', views.ET_new_topic, name='ET_new_topic'),
    path('classification/for_sale/electronics/new_entry/<int:E_T_id>/', views.ET_new_entry, name='ET_new_entry'),
    path('classification/for_sale/electronics/edit_entry/<int:E_E_id>/', views.ET_edit_entry, name='ET_edit_entry'),
    #日常用品
    path('classification/for_sale/necessary/',views.necessary, name='necessary'),
    path('classification/for_sale/necessary/<int:N_T_id>/', views.N_T, name='necessary_topic'),
    path('classification/for_sale/necessary/new_topic/', views.NT_new_topic, name='NT_new_topic'),
    path('classification/for_sale/nacessary/new_entry/<int:N_T_id>/', views.NT_new_entry, name='NT_new_entry'),
    path('classification/for_sale/necessary/edit_entry/<int:N_E_id>/', views.NT_edit_entry, name='NT_edit_entry'),
    

    
]
