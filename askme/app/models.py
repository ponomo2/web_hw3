from django.db import models
from django.contrib.auth.models import User
from django.db.models import QuerySet


class Tag(models.Model):
    tag_id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=50)


class Profile(models.Model):
    avatar = models.ImageField(null=True, blank=True)
    nickname = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Question(models.Model):
    question_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    likes = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    date = models.DateTimeField
    answers_number = models.IntegerField(default=0)

    class HotQuestions(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset().select_related('likes').order_by('-likes', '-date')

    class NewQuestions(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset().order_by('-date')

    class TagQuestions(models.Manager):
        def get_queryset(self, tag_id) -> QuerySet:
            return super().get_queryset().filter(tags__exact=tag_id)

    hot = HotQuestions()
    new = NewQuestions()
    tag = TagQuestions()


class Answer(models.Model):
    answer_id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    correct = models.BooleanField(default=False)


class Likes(models.Model):
    like_or_dislike = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Question', related_name='question_likes', null=True, blank=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, verbose_name='Answer', related_name='answer_likes', null=True, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Author')
