from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    tag_id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=50)


class Profile(models.Model):
    avatar = models.ImageField
    nickname = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Likes(models.Model):
    likes_number = models.IntegerField(default=0)
    dislikes_number = models.IntegerField(default=0)


class Question(models.Model):
    question_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    likes = models.ForeignKey(Likes, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)


class Answer(models.Model):
    answer_id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ForeignKey(Likes, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
