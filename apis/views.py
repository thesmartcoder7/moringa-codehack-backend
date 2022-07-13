from distutils.log import error
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import *
from users.models import User
import jwt, datetime
import re
import sys
import logging


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serialized = UserSerializer(users, many=True)
    return Response(serialized.data)


@api_view(['GET'])
def get_all_students(request):
    users = User.objects.all()
    students = []
    for user in users:
        regex = "@([a-z\S]+)"
        result = re.split(regex, user.email)
        if result[1] == "student.moringaschool.com":
            students.append(user)
    serialized = UserSerializer(students, many=True)
    return Response(serialized.data)



@api_view(['GET'])
def get_mcquestions(request):
    mcquestions = MCQuestion.objects.all()
    serialized = MultipleChoiceSerializer(mcquestions, many=True)
    return Response(serialized.data)



@api_view(['GET'])
def get_mcanswers(request):
    squestions = MCAnswer.objects.all()
    serialized = MultipleChoiceAnswerSerializer(squestions, many=True)
    return Response(serialized.data)



@api_view(['GET'])
def get_kataquestions(request):
    kquestions = KataQuestion.objects.all()
    serialized = KataSerializer(kquestions, many=True)
    return Response(serialized.data)



@api_view(['GET'])
def get_katatests(request):
    ktests = KataTest.objects.all()
    serialized = kataTestSerializer(ktests, many=True)
    return Response(serialized.data)



@api_view(['GET'])
def get_squestions(request):
    squestions = SQuestion.objects.all()
    serialized = SubjectiveSerializer(squestions, many=True)
    return Response(serialized.data)



@api_view(['GET'])
def get_assessments(request):
    assessments = Assessment.objects.all()
    serialized = AssessmentSerializer(assessments, many=True)
    return Response(serialized.data)



@api_view(['GET'])
def get_feedback(request):
    feedback = Feedback.objects.all()
    serialized = FeedbackSerializer(feedback, many=True)
    return Response(serialized.data)



@api_view(['GET'])
def get_invites(request):
    invites = Invite.objects.all()
    serialized = InviteSerializer(invites, many=True)
    return Response(serialized.data)



@api_view(['POST'])
def add_assessment(request):
    new_assessment = {
        "name":request.data['name'],
        "topic":request.data['topic'],
        "time_limit":request.data['time_limit'],
        "pass_mark":request.data['pass_mark'],
        "difficulty":request.data['difficulty'],
        "category":request.data['category']
    }

    serialized = AssessmentSerializer(data=new_assessment)
    if serialized.is_valid():
        serialized.save()
    return Response(serialized.data)



@api_view(['POST'])
def add_feedback(request):
    serialized = FeedbackSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
    return Response(serialized.data)



@api_view(['POST'])
def add_invite(request):
    serialized = InviteSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
    return Response(serialized.data)



@api_view(['GET'])
def get_student_data(request):
    pass



@api_view(['POST'])
def register(request):
    regex = "@([a-z\S]+)"
    result = re.split(regex,request.data['email'])
    if result[1] == "student.moringaschool.com" or result[1] == "moringaschool.com":
        user = User.objects.filter(username=request.data['username']).first()
        if user:
            return Response({'message': 'You have already registered! Please login'})
        else:
            serialized_user = UserSerializer(data=request.data)
            serialized_user.is_valid(raise_exception=True)
            serialized_user.save()
            serialized_user.data.update({'message': 'Success! Please log in'})
            return Response(serialized_user.data)
    else:
        return Response({'message': 'Please register using the school email'})



@api_view(['POST'])
def login(request):
    print("login endpoint is working")
    username = request.data['username']
    password = request.data['password']
    user = User.objects.filter(username=username).first()

    if not user:
        return Response({'message': 'This user is not registered'})

    if not user.check_password(password):
        return Response({'message': 'You have entered the wrong password'})

    payload = {
        'id':user.id,
        'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat':datetime.datetime.utcnow()
    }
    
    token = jwt.encode(payload, 'this87295is9874my8574secret', algorithm='HS256')
    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {'jwt':token}
    print(response.data)
    response.data.update({'message': 'Log in Successful'})
    print("login successful is working")
    return response



@api_view(['GET'])
def authenticated_user(request):
    token = request.COOKIES.get('jwt')
    if not token:
        return Response({'message': 'No authenticated user found!'})
    try:
        payload = jwt.decode(token, 'this87295is9874my8574secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return Response({'message': 'Authentication token expired'})

    user = User.objects.filter(id=payload['id']).first()
    serialized_user = UserSerializer(user)
    serialized_user.data.update({'message': 'User found'})
    return Response(serialized_user.data)



@api_view(['GET'])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'Successful Logout'
    }
    return response



@api_view(['POST'])
def run_code(request):
    action = request.data['action']
    if action == 'run':
        code = request.data['code']
        original_stdout = sys.stdout
        sys.stdout = open('user.txt', 'w')
        exec(code)
        sys.stdout.close()
        sys.stdout = original_stdout 
        output = open('user.txt', 'r').read()
       
        response = {
            'message': 'Code run successfully',
            'output': output
        }
        return Response(response)
    else:
        tests = KataTest.objects.filter(question=KataQuestion.objects.get(id=request.data['question']))
        test_boolean = []
        for test in tests:
            code = (request.data['code'] + '\n')
            original_stdout = sys.stdout
            sys.stdout = open('user.txt', 'w')
            exec(code + f"print({test.test})")
            sys.stdout.close()
            sys.stdout = original_stdout 
            output = open('user.txt', 'r').read()
            test_boolean.append(output.replace('\n', ''))
        return Response({'message': test_boolean})