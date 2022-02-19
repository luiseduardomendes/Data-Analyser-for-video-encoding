import os

class gprof_executer:
    def Call_gprof(self, cfg_encoder, cfg_video, output_dir, video_output_name, qp, frames):
        vtm_dir = "/home/luispmendes/VVCSoftware_VTM/" 

        cfg_dir = vtm_dir + "cfg/"    

        os.system(f'./{vtm_dir}EncoderAppStatic -c {cfg_dir}{cfg_encoder} -c {cfg_dir}{cfg_video} -b \
            {video_output_name}.bin -q {qp} -f {frames} & >>')
        os.system(f'gprof EncoderAppStatic gmon.out >> {output_dir}{video_output_name}.txt')
'''
BasketballDrive_1920x1080_50.yuv           
FourPeople_1280x720_60fps_8bit_420.yuv
BasketballPass_416x240_50.yuv              
Johnny_1280x720_60fps_8bit_420.yuv
BQMall_832x480_60.yuv                      
RaceHorses_416x240_30.yuv
Campfire_3840x2160_30fps_10bit_420.yuv     
RaceHorses_832x480_30.yuv
FoodMarket4_3840x2160_60fps_10bit_420.yuv  
RitualDance_1920x1080_60fps_10bit_420.yuv
'''