from people.models import People
from rest_framework import generics
from people.serializers import PeopleSerializers


class PeopleCreateListView(generics.ListCreateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializers


class PeopleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializers