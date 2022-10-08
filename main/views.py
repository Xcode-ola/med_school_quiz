from django.shortcuts import render
from .models import contact_detail
from .serializer import HomePageSerializer
from rest_framework import generics, permissions, authentication

# Create your views here.
class index(generics.ListAPIView):
    queryset = contact_detail.objects.all()
    serializer_class = HomePageSerializer
    permission_classes = [permissions.IsAuthenticated]

class update(generics.RetrieveUpdateAPIView):
    queryset = contact_detail.objects.all()
    serializer_class = HomePageSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'pk'