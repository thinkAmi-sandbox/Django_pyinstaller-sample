from django.db import models


class Fruit(models.Model):
    name = models.CharField('名前', max_length=50)

    def __str__(self):
        return self.name
