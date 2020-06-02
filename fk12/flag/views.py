from django.shortcuts import render
from user.models import Account
from models import Flag, Plus1, Img, Comment 
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from myapps.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from serializers import FlagSerializer, ImgSerializer, Plus1Serializer, CommentSerializer

# Create your views here.

class FlagViewSet(viewsets.ViewSet):
	def renderMap(self,request):
		queryset = User.objects.all() # need to filter by geographic radius 
		serializer = FlagSerializer(queryset, many=True)
		return Response(serializer.data)


	def FlagDetial(self.request, pk=None):
		queryset = Flags.objects.all()
		