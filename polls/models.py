import datetime

from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', auto_now=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now-datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(
        Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.choice_text


class Vote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(
        Choice, on_delete=models.CASCADE, related_name='votes')
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    votes = models.IntegerField(default=1)

    class Meta:
        unique_together = ("question", "voted_by")

    def __str__(self):
        return '%s(%d)=>%s[%s]' % (self.voted_by, self.votes, self.choice, self.question)
