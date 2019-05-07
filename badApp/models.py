from django.db import models


# Scoreテーブル
class Score(models.Model):
    leftScore = models.IntegerField(default=0)
    rightScore = models.IntegerField(default=0)
    image = models.CharField(max_length=100)
    leftLeft = models.CharField(max_length=100)
    leftRight = models.CharField(max_length=100)
    rightLeft = models.CharField(max_length=100)
    rightRight = models.CharField(max_length=100)
    server = models.CharField(max_length=100, default="")
