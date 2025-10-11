from django.urls import path
from . import views

urlpatterns = [
    path("", views.video_list, name="video-list"),
    path("create/", views.video_create, name="video-create"),
    path("<int:pk>/", views.video_detail, name="video-detail"),
    path("<int:pk>/edit/", views.video_update, name="video-update"),
    path("<int:pk>/delete/", views.video_delete, name="video-delete"),
]
