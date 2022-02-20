import os

class gprof_executer:
    def __init__(self, cfg_encoder, cfg_video, video_name, qp):
        vtm_dir = "/home/luispmendes/VVCSoftware_VTM/"

        cfg_dir = vtm_dir + "cfg/"    
        bin_dir = vtm_dir + "bin/"
        out_dir = vtm_dir + "out/"

        os.system(f'{bin_dir}EncoderAppStatic -c {cfg_dir}{cfg_encoder} \
            -c {cfg_video} -b {out_dir}{video_name}.bin -q {qp} >> {out_dir}log_{video_name}.txt && gprof EncoderAppStatic gmon.out >> {out_dir}{video_name}.txt')


