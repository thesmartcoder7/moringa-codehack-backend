from rest_framework import serializers
from users.models import *
from django.contrib.auth.models import User
from assessment.models import *
from questions.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'


class KataSerializer(serializers.ModelSerializer):
    class Meta:
        model = KataQuestion
        fields = '__all__'



class kataTest(serializers.ModelSerializer):
    class Meta:
        model = KataTest
        fields = '__all__'



class SubjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = SQuestion
        fields = '__all__'



class MultipleChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCQuestion
        fields = '__all__'



class MultipleChoiceAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCAnswer
        fields = '__all__'
