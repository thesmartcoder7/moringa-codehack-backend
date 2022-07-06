from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import *
from users.models import User
import jwt, datetime


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



@api_view(['POST'])
def register(request):
    serialized_user = UserSerializer(data=request.data)
    serialized_user.is_valid(raise_exception=True)
    serialized_user.save()
    return Response(serialized_user.data)



@api_view(['POST'])
def login(request):
    username = request.data['username']
    password = request.data['password']
    user = User.objects.filter(username=username).first()

    if user is None:
        raise AuthenticationFailed('User not found!')

    if not user.check_password(password):
        raise AuthenticationFailed('Incorrect Password')

    payload = {
        'id':user.id,
        'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat':datetime.datetime.utcnow()
    }
    
    token = jwt.encode(payload, 'this87295is9874my8574secret', algorithm='HS256')

    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {'jwt':token}

    return response



@api_view(['GET'])
def authenticated_user(request):
    token = request.COOKIES.get('jwt')
    if not token:
        print('Code gets stuck here')
        raise AuthenticationFailed('Unauthenticated!')
       
    try:

        payload = jwt.decode(token, 'this87295is9874my8574secret', algorithms=['HS256'])
        print('Code goes past the try')
    except jwt.ExpiredSignatureError:
        print('Code goes is riddled with bugs')
        raise AuthenticationFailed('Unauthenticated!')

    user = User.objects.filter(id=payload['id']).first()
    serialized_user = UserSerializer(user)
    return Response(serialized_user.data)



@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'Successful Logout'
    }
    return response