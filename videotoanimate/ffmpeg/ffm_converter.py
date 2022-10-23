import subprocess
class FFMConverter:
    
    def converter_to_ffm(self,input_file,output_file):
        
        try:
            # ffmpeg -i input.mp4 -r 12 -s 320x180 output.gif
            command = "ffmpeg -i " + input_file + " " + "-r 12 -s 320x180 " + output_file 
            subprocess.run(command)
        except:
            print("some exceptions occured")
    
        