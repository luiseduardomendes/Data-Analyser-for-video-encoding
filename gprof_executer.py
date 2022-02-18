import os

class gprof_executer:
    def Call_gprof(self, cfg_encoder, cfg_video, video_path, output_dir, video_output_name, qp, frames):

        vtm_dir = "/home/luispmendes/VVCSoftware_VTM/" 

        cfg_dir = vtm_dir + "cfg/"    

        videos_dir = "/home/videos/"

        os.system(f'./{vtm_dir}EncoderAppStatic -c {cfg_dir}{cfg_encoder} -i {videos_dir}{video_path} -b \
            {video_output_name}.bin -q {qp} -f {frames} & >>')
        os.system(f'gprof EncoderAppStatic gmon.out >> {output_dir}{video_path}.txt')