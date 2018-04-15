from . import models
from django.shortcuts import reverse, render, render_to_response, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from django.contrib.auth.models import User
from rest_framework import authentication, permissions
from rest_framework import generics


class ListResponse(APIView):
    def get(self, request, format=None):
        responses = models.Response.objects.all()
        serializer = serializers.ResponseSerializer(responses, many=True)
        return Response(serializer.data)


'''class DetailCourse(APIView):
    def get(self, request, format=None):
        course = get_object_or_404(_models.Course, pk=request.pk)
        serializer = serializers.CourseSerializer(course)
        return Response(serializer.data)'''


class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)


class ListCreateResponse(generics.ListCreateAPIView):
    queryset = models.Response.objects.all()
    serializer_class = serializers.ResponseSerializer

    def get_queryset(self):
        return self.queryset.filter(survey_id=self.kwargs.get('survey_pk'))

    def perform_create(self, serializer):
        survey = get_object_or_404(
            models.Survey, pk=self.kwargs.get('survey_pk'))
        serializer.save(survey=survey)