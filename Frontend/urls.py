from django.urls import path
from Frontend import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('contacts_page/', views.contacts_page, name='contacts_page'),
    path('contactdatabase/', views.contactdatabase, name='contactdatabase'),
    path('discategory/<itemCatg>/', views.discategory, name='discategory'),
    path('vehicle_show/<int:dataid>/', views.vehicle_show, name='vehicle_show'),
    path('login_page/', views.login_page, name='login_page'),
    path('congratulation_page/', views.congratulation_page, name='congratulation_page'),
    path('register_page/', views.register_page, name='register_page'),
    path('payment_page/<int:dataid>/', views.payment_page, name='payment_page'),
    path('customersave/', views.customersave, name='customersave'),
    path('customerlogin/', views.customerlogin, name='customerlogin'),
    path('customerlogout/', views.customerlogout, name='customerlogout'),
    # path('sort_by/', views.sort_by, name='sort_by'),
    path('display_dealers/<dealname>/', views.display_dealers, name='display_dealers'),

]
