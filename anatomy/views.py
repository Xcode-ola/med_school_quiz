from django.shortcuts import render
from .models import Course_List, Course_Summary, Ana_Answer, Ana_Question, Ana_Quiz
from .serializer import HomePageSerializer, QuizSerializer, SummaryPageSerializer, SummaryOverviewSerializer
from rest_framework import generics, permissions, authentication
from .permissions import IsStaffEditorPermissions
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class index(generics.ListAPIView):
    queryset = Course_List.objects.all()
    serializer_class = HomePageSerializer
    permission_classes = [permissions.IsAuthenticated]

class summary(generics.RetrieveAPIView):
    queryset = Course_Summary.objects.all()
    serializer_class = SummaryPageSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        qs = super().get_queryset()
        if qs is not None:
            return qs.filter(verified = True)
        else:
            return Course_Summary.objects.none()

class summary_overview_list(generics.ListCreateAPIView):
    queryset = Course_Summary.objects.all()
    serializer_class = SummaryOverviewSerializer
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]

class summary_overview_detail(generics.RetrieveUpdateAPIView):
    queryset = Course_Summary.objects.all()
    serializer_class = SummaryOverviewSerializer
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]
    lookup_field = 'pk'

class StartQuiz(APIView):
    def get(self, request, format=None, **kwargs):
        question = Ana_Question.objects.filter(chapter__id = kwargs['pk'])
        serializer = QuizSerializer(question, many=True)
        return Response(serializer.data)
