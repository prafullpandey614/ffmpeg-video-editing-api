from .models import VideoFile
from .ffm_converter import FFMConverter



def convert(input_file,output_file,pk):
    # TODO : Subprocess FFMPEG Commands
    print("I am here")
    file = FFMConverter()
    file.converter_to_ffm(input_file,output_file)

    save_to_database(pk)
    print("Called Saved To Database")
def save_to_database(pk):
    
    filed = VideoFile.objects.get(pk=pk)
    print(filed.file)
    filed.file = f'/uploads/output{pk}.gif'
    filed.save()
    