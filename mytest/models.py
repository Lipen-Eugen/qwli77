from django.db import models



class MapsPointModel(models.Model):
    pointerdolgota = models.FloatField()
    pointershirota = models.FloatField()

    def __str__(self):
        return str(self.id)
