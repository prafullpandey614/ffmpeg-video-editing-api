
from celery import shared_task
from .models import VideoFile
from . import util_functions
@shared_task(bind=True)
def test_func(self,pk):
    #operations
    print(pk)
    input_file  = VideoFile.objects.get(id=pk)
    util_functions.convert( 'uploads/'+str(input_file.file) , f'uploads/uploads/output{pk}.gif',pk) #this method is defined under util_functions.py
        
    print("Working")
    for i in range(10):
        print(i)
    return "Done"