from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)


class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return f"/update_persons/{self.pk}/"


def check_year(value):
    if value < 1900:
        raise ValidationError("podany rok jest za mały powinnien być większy niz 1899")


class Movie(models.Model):
    title = models.CharField(max_length=128, )
    year = models.IntegerField(null=True, verbose_name='rok', validators=[check_year])
    director = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='directed_by', verbose_name='reżyser')
    screen_play = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='written_by', null=True,
                                    verbose_name='scenażysta')
    category = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('update_movie', args=(self.id,))

PRODUCERS = (
    (1, 'Netflix'),
    (2, 'HBO'),
    (3, 'Amazon'),
    (4, 'Disney'),
)

class TvShow(models.Model):
    title = models.CharField(max_length=128)
    year = models.IntegerField()
    director = models.ForeignKey(Person, on_delete=models.CASCADE)
    owner = models.IntegerField(choices=PRODUCERS)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_tvshow', args=(self.id,))