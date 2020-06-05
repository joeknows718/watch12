from rest_framework import serializers
from django.contrib.auth.models import User
from models import Account, Refernece




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email')



class AccountSerializer(serializers.ModelSerializer):
	

	user =  UserSerializer(required=True)
	flags = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	plus1s = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	disputes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	comments= serializers.PrimaryKeyRelatedField(many=True, read_only=True)



	class Meta:
		model =  Account
		fields =  ('user','flags','disputes','plus1s','comments')

		def create(self, validated_data):
			user_data = validated_data.pop('user')
			user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        	account, created = Account.objects.update_or_create(user=user)
        	return account 

class ReferenceSerializer(serializers.ModelSerializer)
	class Meta:
		model = Reference
		fields =  ('refered', 'referrer')













