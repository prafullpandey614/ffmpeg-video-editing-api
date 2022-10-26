from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView , RetrieveAPIView
from rest_framework.decorators import api_view
from .models import VideoFile
from .serializers import VideoSerializer
from .tasks import Converter

class ApiOverView(APIView):
    
    def get(self,request,pk=None,format=None):
        api_urls = {
            'upload-file' : '/upload-file/',
            'download-file' : '/download-file/'
        }
        return Response(api_urls)
    
    
class FileUpload(CreateAPIView):
    queryset = VideoFile.objects.all()
    serializer_class = VideoSerializer
    
    
    

class FileConvert(APIView):
    
    
    def get(self,request,pk):
        
        Converter.delay(pk) #Celery Worker will do the tasks
        return Response("Hold On! Video Transcoding in process")
    
    
class RetrieveFileView(RetrieveAPIView):
    queryset = VideoFile.objects.all()
    serializer_class = VideoSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk) 

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #     def post(self,request):
        
#         # print(request.data)
#         # try:
#         #     file = request.data['file']
#         # except:
#         #     print("exception occured")
#         serializer = VideoSerializer(data=request.data, many=True)
        
#         if serializer.is_valid():
#             serializer.save()
#             print(serializer.data)
#             # data = FFMConverter()
#             # data.converter.ffm(request.input,f"uploads/new/{request.input}")
        
            
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)