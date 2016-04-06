from django.db import models

# Create your models here.
class Res(models.Model):
    name=models.CharField(max_length=20)
    version=models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=['name']

class Meun(models.Model):
    menu1=models.CharField(max_length=20)
    menu2=models.CharField(max_length=20)
    res=models.ForeignKey(Res)

    def __str__(self):
        return self.menu1
