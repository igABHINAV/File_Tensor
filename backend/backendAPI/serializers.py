from rest_framework import serializers
from .models import Files , Folder
import shutil
from rest_framework.response import Response



class Fileserializer(serializers.Serializer):
    files = serializers.ListField(
        child = serializers.FileField(max_length = 10000 , allow_empty_file=False , use_url = False)
        )
    folder = serializers.CharField(required = False)

    def create(self, validated_data):
        folder = Folder.objects.create()
        files = validated_data.pop('files')
        arr= []
        for file in files :
            obj = Files.objects.create(folder=folder , file=file)
            arr.append(obj)
        shutil.make_archive(f'media/zipfiles/{folder.uid}' , 'zip' , f'media/{folder.uid}/')
        
        return {"files":files , "folder":str(folder.uid)  }


        