import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from hello.models import Message
from hello.serializers.serializers import MessageSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger(__name__)

def home(request):
    return HttpResponse("Hello, Django!")

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_messages(request):
    user = request.user.email
    logger.info(user)
    messages = Message.objects.filter(to_user=user)
    serializer = MessageSerializer(messages, many=True)
    return JsonResponse({'messages': serializer.data}, safe=False, status=status.HTTP_200_OK)
