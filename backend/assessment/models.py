from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User



DIFFICULTY_LEVELS = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)


class Assessment(models.Model):
    name = models.CharField(max_length=3000)
    topic = models.CharField(max_length=500)
    time_limit = models.PositiveIntegerField(help_text='duration of assessment in minutes')
    pass_mark = models.PositiveIntegerField(help_text='score in %')
    difficulty = models.CharField(max_length=6, choices=DIFFICULTY_LEVELS)

    def __str__(self):
        return f"{self.name} - {self.topic}"
    
    def get_questions(self):
        """
        This gets all the questions that 
        are related to this Assessment 
        through the reverse relationship
        """
        return self.question_set.all()



class Question(models.Model):
    text = models.TextField()
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        """ 
        This method basically gets all the answers 
        that are related to this question throu
        reverse relationship
        """
        return self.answer_set.all()



class Answer(models.Model):
    text = models.TextField()
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"



class Grade(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()
    
    def __str__(self):
        return str(self.pk)


class Feedback(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.TextField()

    def __str__(self):
        return f"Feedback for {self.student.username.title()} on {self.assessment}"

    class Meta:
        verbose_name_plural = 'Feedback'