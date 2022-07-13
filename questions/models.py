from django.db import models
from assessment.models import Assessment

# Create your models here.
class MCQuestion(models.Model):
    question = models.TextField()
    assessment = models.ManyToManyField(Assessment, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.question)

    def get_answers(self):
        """ 
        This method basically gets all the answers 
        that are related to this question throu
        reverse relationship
        """
        return self.mcanswer_set.all()

    class Meta:
        verbose_name_plural = 'Multiple Choice Questions'



class MCAnswer(models.Model):
    answer = models.CharField(max_length=5000)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(MCQuestion, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"question: {self.question.text}, answer: {self.answer}, correct: {self.correct}"

    class Meta:
        verbose_name_plural = 'Multiple Choice Answers'



class KataQuestion(models.Model):
    question = models.TextField()
    assessment = models.ManyToManyField(Assessment, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    starter_code = models.TextField(blank=True, null=True)
    all_tests_passed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.question)

    def get_tests(self):
        """ 
        This method basically gets all the tests 
        that are related to this kata through
        reverse relationship
        """
        return self.katatest_set.all()



class KataTest(models.Model):
    test = models.CharField(max_length=5000, help_text='Create a test for your kata question')
    question = models.ForeignKey(KataQuestion, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"question: {self.question.question}, testcase: {self.test}"




class SQuestion(models.Model):
    question = models.TextField()
    assessment = models.ManyToManyField(Assessment, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    response = models.TextField(blank=True, null=True)
    marked_as_right = models.BooleanField(default=False)

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name_plural = 'Subjective Questions'



