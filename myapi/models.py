from django.db import models


class Client(models.Model):
    clientName = models.CharField(max_length=100)
    clientCountry = models.CharField(max_length=100)

    def __str__(self):
        return self.clientName


class Project(models.Model):
    projectName = models.CharField(max_length=100)
    projectLanguage = models.CharField(max_length=100)
    projectClient = models.IntegerField()

    def __str__(self):
        return self.projectName