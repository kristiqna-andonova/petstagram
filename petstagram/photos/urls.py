from django.urls import path, include
from petstagram.photos import views

urlpatterns = (
    path('add/', views.add_photo, name='add_photo'),
    path('<int:pk>/', include([
        path('', views.show_photo_details, name='show_photo'),
        path('edit/', views.edit_photo, name='edit_photo')
    ]))
)