from django.urls import path
from Backend import views

urlpatterns = [
    path('indexpage/', views.indexpage, name='indexpage'),
    path('vehicles_category/', views.vehicles_category, name='vehicles_category'),
    path('vehicles_category_form/', views.vehicles_category_form, name='vehicles_category_form'),
    path('display_vehicles_category/', views.display_vehicles_category, name='display_vehicles_category'),
    path('edit_vehicles_category/<int:dataid>', views.edit_vehicles_category, name='edit_vehicles_category'),
    path('update_vehicles_category/<int:dataid>', views.update_vehicles_category, name='update_vehicles_category'),
    path('delete_vehicles_category/<int:dataid>', views.delete_vehicles_category, name='delete_vehicles_category'),
    path('add_vehicles/', views.add_vehicles, name='add_vehicles'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('display_vehicles/', views.display_vehicles, name='display_vehicles'),
    path('edit_vehicles/<int:dataid>', views.edit_vehicles, name='edit_vehicles'),
    path('update_vehicles/<int:dataid>', views.update_vehicles, name='update_vehicles'),
    path('delete_vehicles/<int:dataid>', views.delete_vehicles, name='delete_vehicles'),
    path('display_contacts/', views.display_contacts, name='display_contacts'),
    path('delete_contacts/<int:dataid>', views.delete_contacts, name='delete_contacts'),
    path('adminpage/', views.adminpage, name='adminpage'),
    path('adminpagedb/', views.adminpagedb, name='adminpagedb'),
    path('displayadminpg/', views.displayadminpg, name='displayadminpg'),
    path('editadmin/<int:dataid>', views.editadmin, name='editadmin'),
    path('updateadminpage/<int:dataid>', views.updateadminpage, name='updateadminpage'),
    path('deleteadmin/<int:dataid>', views.deleteadmin, name='deleteadmin'),
    path('logindata/', views.logindata, name='logindata'),
    path('logindb_fun/', views.logindb_fun, name='logindb_fun'),
    path('customerlogout/', views.customerlogout, name='customerlogout'),

]
