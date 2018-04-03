from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
# Create your models here.
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])  # 得到所有的编程语言
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())  # 得到所有的配色风格

class MusicSubType(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=100, default='')

    def __str__(self):
        return "music_sub_type: %s" % self.name

class MusicType(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=100, default='')
    music_sub_type = models.ManyToManyField(MusicSubType)

    def __str__(self):
        return "music_type: %s" % self.name

class Album(models.Model):
    name = models.CharField(max_length=50)
    singer = models.CharField(max_length=80, default='')
    desc = models.CharField(max_length=100, default='')
    music_type = models.ManyToManyField(MusicType)

    def __str__(self):
        return "album: %s" % self.name




