from django.db import models
from assessment.models import Assessment

# Create your models here.
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

    class Meta:
        verbose_name_plural = 'Multiple Choice Questions'



class MCAnswer(models.Model):
    text = models.TextField()
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(MCQuestion, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"

    class Meta:
        verbose_name_plural = 'Multiple Choice Answers'



class SQuestion(models.Model):
    text = models.TextField()
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    marked_as_right = models.BooleanField(default=False)

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name_plural = 'Subjective Questions'



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
