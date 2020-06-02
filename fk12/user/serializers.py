from rest_framework import serializers
from django.contrib.auth.models import User
from models import Account, Refernece  



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username')



class AccountSerializer(serializers.ModelSerializer):
	

	user =  UserSerializer(required=True)
	class Meta:
		model =  Account
		fields =  ('user')

		def create(self, validated_data):
			user_data = validated_data.pop('user')
			user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        	account, created = Account.objects.update_or_create(user=user)
        	return account 

class ReferenceSerializer(serializers.ModelSerializer)
	class Meta:
		model = Reference
		fields =  ('refered', 'referrer')













