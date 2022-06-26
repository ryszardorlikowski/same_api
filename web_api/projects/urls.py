from django.urls import path

from web_api.projects.views import create_project

urlpatterns = [
    path('/create', create_project)
]
