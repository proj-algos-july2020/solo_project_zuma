from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_user', views.create_user),
    path('login', views.login),
    path('dashboard', views.dashboard),
    path('trips/new', views.new_trip),
    path('trips/create', views.create_trip),
    # path('trips/like_trip/<int:trip_id>', views.like_trip),
    # path('trips/delete_like/<int:trip_id>', views.delete_like),
    # path('trips/<int:id>/delete', views.destroy),
    # path('trips/edit/<int:id>', views.edit_trip),
    # path('trips/update/<int:id>', views.update),
    # path('trips/grant/<int:trip_id>', views.grant),
    path('log_out', views.log_out),
]