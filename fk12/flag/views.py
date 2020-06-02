from django.shortcuts import render
from user.models import Account
from models import Flag, Plus1, Img, Comment 
from serializers import FlagSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
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
		flag = get_object_or_404(queryset, pk=pk)
		#needs to query associated comments and plus 1 count and list of 
		#+1 users 

	def NewFlag(self.request):
		#need to unpack and format to be submitted to serializer
		#title = request.title
		#account = request.account
		#lon =  request.lon
		#lat = request.lat
		#notes =  request.notes
		#precint =  request.precint
		#badge_num =  request.badge_num
		new_flag = FlagSerializer()
		new_flag.account.update_trust()#runs model method to update trust
		new_flag.account.trust_check()
		return new_flag#runs model method to check trust





		
