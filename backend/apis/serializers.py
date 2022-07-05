from rest_framework import serializers
from users.models import *
from users.models import User
from assessment.models import *
from questions.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password'
        ]
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def create(self, validated_data):
        """ This function overwrites the default user creation function"""
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            """ The set_password method is a django auth method for hashing passwords """
            instance.set_password(password)
        instance.save()
        return instance



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
