from django.db import models
from questions.models import MCQuestion, SQuestion, KataQuestion
from django.contrib.auth.models import User

# Create your models here.
class MCFeedback(models.Model):
    question = models.ForeignKey(MCQuestion, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.TextField()

    def __str__(self):
        return f"Feedback for {self.student.username.title()} on {self.question}"

    class Meta:
        verbose_name_plural = 'Multiple Choice Feedback'


class SFeedback(models.Model):
    question = models.ForeignKey(SQuestion, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.TextField()

    def __str__(self):
        return f"Feedback for {self.student.username.title()} on {self.question}"

    class Meta:
        verbose_name_plural = 'Subjective Feedback'


class KataFeedback(models.Model):
    question = models.ForeignKey(KataQuestion, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.TextField()

    def __str__(self):
        return f"Feedback for {self.student.username.title()} on {self.question}"

    class Meta:
        verbose_name_plural = 'Kata Feedback'

