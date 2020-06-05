from django.shortcuts import render
from user.models import Account
from models import Flag, Plus1, Img, Comment 
from serializers import FlagSerializer, ImgSerializer, Plus1Serializer, CommentSerializer, DisputeSerializer
from datetime import datetime, timedelta
from django.http import Http404, Http403
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


#list 12 hours of flags for map | Create a new flag
class FlagView(APIView):
	def get(self, request, format=None):
		time_threshold = datetime.now() - timedelta(hours=12)
		flags = Flag.objects.filter(date__lt=time_threshold, disputed=False) # need to filter by geographic radius 
		serializer = FlagSerializer(flags, many=True)
		return Response(serializer.data)


	@permission_classes([IsAuthenticated])
	def post(self, request, format=None):
		serializer = FlagSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class FlagDetail(APIView):
	def get_object(self,pk)
		try:
			return Flag.objects.get(pk=pk)
		except Flag.DoesNotExist:
			raise Http404
	#Can we look into how to make sure we can access a count of the flag in question
	def get(self, request, pk, format=None):
		flag = self.get_object(pk)
		serializer = FlagSerializer(flag)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		flag = self.get_object(pk)
		if request.user == flag.account.user:
			serializer = SnippetSerializer(snippet, data=request.data)
   			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		else:
			raise Http403

	 def delete(self, request, pk, format=None):
	 	flag = self.get_object(pk)
	 	if request.user == flag.account.user:
			flag.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		else:
			raise Http403


class Plus1Views(APIView):
	def get(self, request, format=None):
		plus1 = Plus1.objects.filter(flagID=request.data['flag']) # need to filter by associated flagID
		serializer = Plus1Serializer(plus1)
		return Response(serializer.data)


	@permission_classes([IsAuthenticated])
	def post(self, request, format=None):
		serializer = Plus1Serializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			Account = Account.objects.filter(pk=request.data['flag_poster'])
			Account.update_trust()
			Account.trust_check()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	@permission_classes([IsAuthenticated])
	def delete(self, request, pk, format=None):
	 	plus1 = plus1.get_object(pk)
	 	if request.user == plus1.account.user:
			img.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		else:
			raise Http403

class CommentViews(APIView):
	def get(self, request, format=None):
		comment = Comment.objects.filter(flagID=request.data['flag']) # need to filter by associated flagID
		serializer = CommentSerializer(comment)
		return Response(serializer.data)


	@permission_classes([IsAuthenticated])
	def post(self, request, format=None):
		serializer = CommentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	@permission_classes([IsAuthenticated])
	def delete(self, request, pk, format=None):
	 	comment = Comment.get_object(pk)
	 	if request.user == comment.account.user:
			img.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		else:
			raise Http403

class ImgView(APIView)
	def get(self, request, format=None):
		img = img.objects.filter(flagID=request.data['flag']) # need to filter by associated flagID
		serializer = ImgSerializer(comment)
		return Response(serializer.data)

	@permission_classes([IsAuthenticated])
	def post(self, request, format=None):
		serializer = ImgSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	@permission_classes([IsAuthenticated])
	def delete(self, request, pk, format=None):
	 	img = Img.get_object(pk)
	 	if request.user == img.flag.account.user:
			img.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		else:
			raise Http403

class DisputeView(APIView):

	def get(self, request, format=None):
		dispute = Dispute.objects.filter(flagID=request.data['flag']) # need to filter by associated flagID
		serializer = DisputeSerializer(comment)
		return Response(serializer.data)

	@permission_classes([IsAuthenticated])
	def post(self, request, format=None):
		serializer = DisputeSerializer(data=request.data)
		if serializer.is_valid()
			serializer.save()
			flag = Flag.objects.filter(flagID=request.data['flag'])
			flag.dispute_checks()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	@permission_classes([IsAuthenticated])
	def delete(self, request, pk, format=None):
	 	dispute = Dispute.get_object(pk)
	 	if request.user == dispute.account.user:
			img.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		else:
			raise Http403