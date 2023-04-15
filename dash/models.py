from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class Singer(models.Model):
    img = models.ImageField(upload_to="singers/")
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=200)
    singer = models.ForeignKey("Singer", on_delete=models.CASCADE)
    img = models.ImageField(upload_to="albums/")

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=100)
    audio_file = models.FileField(blank=True, null=True)
    img = models.ImageField(upload_to="songs/")
    time = models.DurationField()
    album = models.ForeignKey("Album", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Like(models.Model):
    """
    Adding song model
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "song")


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_singer(sender, instance, created, **kwargs):
#     if created and instance.is_singer:
#         Singer.objects.create(name=instance.email)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_singer(sender, instance, **kwargs):
    if instance.is_singer and not instance.singer:  # Add check to ensure Singer object is not created again
        instance.singer = Singer(name=instance.email)
        instance.singer.save()


