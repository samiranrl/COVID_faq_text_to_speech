from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length = 500)
    answer_text = models.CharField(max_length = 2000)
    language = models.CharField(max_length = 50)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.question_text
