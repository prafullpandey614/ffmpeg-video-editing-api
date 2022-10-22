from .models import VideoFile
from .ffm_converter import FFMConverter
import sys
# from .output import output
# sys.path.append(r'C:\Users\prafu\Desktop\tigbar\videotoanimate\output')

def convert(input_file,output_file,pk):
    #TODO : Subprocess FFMPEG Commands
    
    file = FFMConverter()
    file.converter_to_ffm(input_file,output_file)
    # file.converter_to_ffm('uploads/22/myvideo.mp4',f'output/output.gif')
    save_to_database(pk)
    print("Called Saved To Database")
def save_to_database(pk):
    # file = VideoFile()
    filed = VideoFile.objects.get(pk=pk)
    print(filed.file)
    filed.file = '/uploads/output.gif'
    filed.save()
    # print(filed.file)
    # if filed.is_valid():
    #     filed.save()
    #     print("Saved to Database")
    # else:
    #     print("Not Saved")