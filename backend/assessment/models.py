from django.db import models
from users.models import User



DIFFICULTY_LEVELS = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)

CATEGORIES = (
    ('multiple_choice', 'multiple_choice'),
    ('kata', 'kata'),
    ('subjective', 'subjective')
)


class Assessment(models.Model):
    name = models.CharField(max_length=3000)
    topic = models.CharField(max_length=500)
    time_limit = models.PositiveIntegerField(help_text='Duration of assessment in minutes')
    pass_mark = models.PositiveIntegerField(help_text='Pass Score in %')
    difficulty = models.CharField(max_length=6, choices=DIFFICULTY_LEVELS)
    category = models.CharField(max_length=20, choices=CATEGORIES, null=True)

    def __str__(self):
        return f"{self.name} - {self.topic}"
    
    def get_questions(self):
        """
        This gets all the questions that 
        are related to this Assessment 
        through the reverse relationship
        """
        return self.mcquestion_set.all()

    def get_katas(self):
        """
        This gets all the kata questions that 
        are related to this assessment through
        the reverse relationship
        """
        return self.kataquestion_set.all()

    def get_subjective(self):
        """
        This gets all the subjective questions that 
        are related to this assessment through
        the reverse relationship
        """
        return self.squestion_set.all()



class Grade(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()
    
    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = 'Student Grades'



class Feedback(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.TextField()

    def __str__(self):
        return f"Feedback for {self.student.username.title()} on {self.assessment}"

    class Meta:
        verbose_name_plural = 'Feedback'




class Invite(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    users = models.TextField(help_text='Add student emails separated by spaces')

    class Meta:
        verbose_name_plural = 'All Invites'