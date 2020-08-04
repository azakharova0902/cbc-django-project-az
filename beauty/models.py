from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/%y/%m/%d', default = 'some string')
    price = models.CharField(max_length=40)
    description = models.TextField()
    duration = models.CharField(max_length=20, blank=True)
    performed_by = models.ManyToManyField('Technician')

    def __str__ (self):
        return self.name

class Technician(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/%y/%m/%d', default = 'some string')
    expertise = models.CharField(max_length=50)
    story = models.TextField()

    def __str__ (self):
        return self.name