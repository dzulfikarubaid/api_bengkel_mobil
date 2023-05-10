from django.db import models

# Create your models here.
class ServisModel(models.Model):
    id = models.AutoField(primary_key=True)
    dibuat_pada = models.DateField(auto_now_add=True)
    keluhan = models.TextField()

    def __str__(self):
        return str(self.id) + " | "+self.keluhan