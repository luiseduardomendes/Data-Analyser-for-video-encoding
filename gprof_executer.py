import os

class gprof_executer:
    def __init__(self, cfg_encoder, cfg_video, output_dir, video_output_name, qp):
        vtm_dir = "/home/luispmendes/VVCSoftware_VTM/" 

        cfg_dir = vtm_dir + "cfg/"    
        bin_dir = vtm_dir + "bin/"

        print(f'.{bin_dir}EncoderAppStatic -c {cfg_dir}{cfg_encoder} \
            -c {cfg_video} -b {video_output_name}.bin -q {qp} & >>')
        input('')
        #os.system(f'.{bin_dir}EncoderAppStatic -c {cfg_dir}{cfg_encoder} \
        #    -c {cfg_video} -b {video_output_name}.bin -q {qp} & >>')
        #os.system(f'gprof EncoderAppStatic gmon.out >> {output_dir}{video_output_name}.txt')


