from django.db import models
from django.contrib.auth.models import User



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



class MCQuestion(models.Model):
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
        return self.mcanswer_set.all()



class MCAnswer(models.Model):
    text = models.TextField()
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(MCQuestion, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"



class SQuestion(models.Model):
    text = models.TextField()
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    marked_as_right = models.BooleanField(default=False)

    def __str__(self):
        return str(self.text)



class KataQuestion(models.Model):
    text = models.TextField()
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    all_tests_passed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.text)

    def get_tests(self):
        return self.katatest_set.all()



class KataTest(models.Model):
    text = models.CharField(max_length=5000)
    question = models.ForeignKey(KataQuestion, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"question: {self.question.text}, testcase: {self.text}"



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