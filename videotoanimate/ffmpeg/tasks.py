from celery import shared_task
from .models import VideoFile
from . import util_functions
@shared_task(bind=True)
def Converter(self,pk):
    #operations
    
    input_file  = VideoFile.objects.get(id=pk)
    util_functions.convert( 'uploads/'+str(input_file.file) , f'uploads/uploads/output{pk}.gif',pk) #this method is defined under util_functions.py
        
    print("Working")
    return "Completed"