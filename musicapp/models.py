from django.db import models

# Create your models here.
class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Artiste(AbstractBaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Song(AbstractBaseModel):
    artist = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date_released = models.DateField()
    likes = models.IntegerField()

    def __str__(self):
        return self.title


class Lyric(AbstractBaseModel):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content[:10]
