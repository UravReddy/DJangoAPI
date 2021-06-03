from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ClientSerializer,ProjectSerializer
from .models import Client,Project
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated

#Class to view all clients with filter
class ClientFilterSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    #filter_fields = ('clientCountry',)
    
#Deleting a client by id
def delete_client(request,id):
    obj = get_object_or_404(Client,id=id)
    obj.delete()
    return HttpResponse('<h1> Client Deleted </h1>')

#Sort deleting clients by country
def ClientDeleteByCountry(request,area):
    queryset = Client.objects.filter(clientCountry=area)
    for x in queryset:
        obj = get_object_or_404(Client,id=x.id)
        obj.delete()
        print(x.id)
    return HttpResponse('<h1> Deleted Clients From :{} </h1>'.format(area))


#Class to view all projects with filters for Client Id's and Language
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer
   # filter_fields = ('projectClient','projectLanguage',)

#Delete a project by id
def delete_project(request,id):
    obj = get_object_or_404(Project,id=id)
    obj.delete()
    return HttpResponse('<h1> Project Deleted </h1>')

#Sort delete projects by language
def ProjectDeleteByLanguage(request,language):
    queryset = Client.objects.filter(projectLanguage=language)
    for x in queryset:
        obj = get_object_or_404(Project,id=x.id)
        obj.delete()
    return HttpResponse('<h1> Deleted Projects With The Language :{} </h1>'.format(language))

