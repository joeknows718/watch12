from rest_framework import serializers
from user.serializers import AccountSerializer
from models import Flag, Plus1, Comment 







class FlagSerializer(serializers.ModelSerializer):
		pluses = serializers.RelatedField(many=True)
		comments = serializers.RelatedField(many=True)
		imgs = serializers.RelatedField(many=True)
	    class Meta:
       		model = Flag 
       		fields = ('title', 'account', 'log', 'lat', 'notes', 'preinct', 'badge_num', 'pluses', 'comments')


class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ('text')

class Plus1Serializer(serializers.ModelSerializer):
	class Meta:
		model = Plus1

class ImgSerializer(serializers.Serializer):
	photo_url = serializers.SerializerMethodField()

	class Meta:
		model = Img
		fields = 'photo_url'







