from django.db import models
from django.db.models.fields import CharField, DateTimeField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
import os.path, datetime

def image_dir(instance, filename):
    return os.path.join("images", "image_%s%s" % (
        datetime.datetime.now().isoformat().replace(":", "-"),
        os.path.splitext(filename)[1]))
    
def sound_dir(instance, filename):
    return os.path.join("sound", "sound_%s%s" % (
        datetime.datetime.now().isoformat().replace(":", "-"),
        os.path.splitext(filename)[1]))



# Create your models here.
class Device(models.Model):
    user = ForeignKey(User)
    device_type = CharField(max_length=255)
    name = CharField(max_length=255)
    uuid = CharField(max_length=255)
    api_key = CharField(max_length=255)

class Sighting(models.Model):
    latitude = CharField(max_length=255)
    longitude = CharField(max_length=255)
    image = models.ImageField(upload_to=image_dir)
    sound = models.FileField(upload_to=sound_dir)
    device = ForeignKey(Device)
    time = DateTimeField()
    