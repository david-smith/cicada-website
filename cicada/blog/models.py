from django.db import models
from django.contrib.auth.models import User

# Create your models here.
   
class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length = 100)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.title

    
    