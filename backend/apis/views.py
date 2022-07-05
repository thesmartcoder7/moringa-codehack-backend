from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import *
from django.contrib.auth.models import User


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serialized = UserSerializer(users, many=True)
    return Response(serialized.data)


@api_view(['GET'])
def get_mcquestions(request):
    mcquestions = MCQuestion.objects.all()
    serialized = MultipleChoiceAnswerSerializer(mcquestions, many=True)
    return Response(serialized.data)


@api_view(['GET'])
def get_squestions(request):
    squestions = SQuestion.objects.all()
    serialized = MultipleChoiceAnswerSerializer(squestions, many=True)
    return Response(serialized.data)


@api_view(['GET'])
def get_kataquestions(request):
    kquestions = KataQuestion.objects.all()
    serialized = KataSerializer(kquestions, many=True)
    return Response(serialized.data)


@api_view(['GET'])
def get_assessments(request):
    assessments = Assessment.objects.all()
    serialized = MultipleChoiceAnswerSerializer(assessments, many=True)
    return Response(serialized.data)


@api_view(['POST'])
def add_assessment(request):
    serialized = AssessmentSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
    return Response(serialized.data)