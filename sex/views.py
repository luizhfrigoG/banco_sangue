from sex.models import Sex
from rest_framework import generics
from sex.serializers import SexSerializer


class SexCreateListView(generics.ListCreateAPIView):
    queryset = Sex.objects.all()
    serializer_class = SexSerializer

class SexRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sex.objects.all()
    serializer_class = SexSerializer
