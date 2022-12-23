from django.db import models
from django.db.models.fields import AutoField

# Create your models here.
GENRE_CHOICES = [
    ('Horror','horror'),
    ('Sci-fi','sci-fi'),
    ('Thriller','thriller'),
    ('Action','action'),
    ('Comedy','comedy'),
    ('Sports','sports'),
]
class MovieBank(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,null=True)
    genre = models.CharField(choices=GENRE_CHOICES,max_length=100)
    language = models.CharField(max_length=100)
    movie_type = models.CharField(max_length=100)
    rating = models.IntegerField()
    release_date = models.DateField()
    collection = models.DecimalField(decimal_places=2,max_digits=4)
    director = models.CharField(max_length=100)
    
    class Meta:
         verbose_name = "The movie data"
         ordering = ['movie_id']

    def __str__(self):
        if self.title:
            return self.title
        return "No title-"+' '+self.genre