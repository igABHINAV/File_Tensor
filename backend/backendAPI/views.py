from rest_framework.response import Response
from rest_framework.decorators import api_view , parser_classes
from .serializers import Fileserializer
from .models import Files , Folder
# Create your views here.

@api_view(['POST'])
def uploadfiles(req) :
    try :
        serializer = Fileserializer(data=req.data)
        if serializer.is_valid() :
            serializer.save()

            return Response({
                "message":"object saved successfully",
                "data":serializer.data,
            })
        else :
            return Response({
                "error":"Something went wrong!"
            })
    except Exception as e :
        print(e)