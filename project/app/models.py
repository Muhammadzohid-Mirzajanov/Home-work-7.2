from django.db import models

class Janr(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    janr = models.ForeignKey(Janr,on_delete=models.CASCADE)
    year = models.IntegerField()

    def __str__(self):
        return self.name
    