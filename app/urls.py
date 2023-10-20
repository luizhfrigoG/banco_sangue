from django.contrib import admin
from django.urls import path
from people.views import PeopleCreateListView, PeopleRetrieveUpdateDestroyView
from sex.views import SexCreateListView, SexRetrieveUpdateDestroyView
from type.views import TypeCreateListView, TypeRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('people/', PeopleCreateListView.as_view(), name= 'people-create-list'),
    path('people/<int:pk>/', PeopleRetrieveUpdateDestroyView.as_view(), name= 'people-detail-view'),

    path('sex/', SexCreateListView.as_view(), name= 'sex-create-list'),
    path('sex/<int:pk>/', SexRetrieveUpdateDestroyView.as_view(), name= 'sex-detail-view'),

    path('type/', TypeCreateListView.as_view(), name= 'type-create-list'),
    path('type/<int:pk>/', TypeRetrieveUpdateDestroyView.as_view(), name= 'type-detail-view'),
]
