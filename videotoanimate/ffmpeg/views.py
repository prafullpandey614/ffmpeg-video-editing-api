from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from . import util_functions
from .models import VideoFile
from .serializers import VideoSerializer
from .tasks import test_func

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
        
        test_func.delay(pk)
        # input_file  = VideoFile.objects.get(id=pk)
        # util_functions.convert( 'uploads/'+str(input_file.file) , f'uploads/uploads/output{pk}.gif',pk) 
        #this method is defined under util_functions.py   
    
        
        output_file = VideoFile.objects.get(id=pk)
        
        
        serializer = VideoSerializer(output_file)
        
        return Response(serializer.data)
        
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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