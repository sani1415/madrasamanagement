from django.db import models

class ClassRoom(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

