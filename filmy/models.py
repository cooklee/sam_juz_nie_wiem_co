from django.db import models



# Create your models here.
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=32)


class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return f"/update_persons/{self.pk}/"
        return reverse("update_persons", args=(self.pk,))


class Movie(models.Model):
    title = models.CharField(max_length=128)
    director = models.ForeignKey(Person, on_delete=models.CASCADE)
