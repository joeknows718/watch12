from django.shortcuts import render
from models import Account, Reference 
from serializers import UserSerializer, AccountSerializer, ReferenceSerializer
from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	UpdateAPIView,
	RetrieveAPIView
	RetrieveUpdateAPIView
	)
from rest_framework.views import APIView

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly

	)

class UserCreateAPIView(APIView):
	serializer_class = UserSerializer
	queryset = Users.objects.all()

# Create your views here.
class AccountCreateAPIView(APIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class ReferalAPIView(APIView):
	permission_classes = (IsApproved,)
	queryset = Account.objects.all()
    serializer_class = ReferalSerializer

	@permission_classes([IsAuthenticated])
		def post(self, request, format=None):
			serializer = ReferalSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				Referal.refered.reference_check()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
