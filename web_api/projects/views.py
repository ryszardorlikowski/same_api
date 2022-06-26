from django.http import HttpRequest
from injector import inject
from rest_framework.decorators import api_view
from rest_framework.response import Response

from projects.application.use_cases.create_project import CreateProject


@api_view(['GET'])
def create_project(request: HttpRequest, create_project_us: CreateProject):
    return Response('test')
