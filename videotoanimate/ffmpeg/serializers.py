from dataclasses import fields
from rest_framework import serializers
from .models import VideoFile
class VideoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=  VideoFile
        fields = "__all__"
        
#     def create(self,validated_data):
#         return VideoFile.objects.create(**validated_data)
# class FileSerializer():
    