import os

class gprof_executer:
    def __init__(self, cfg_encoder: str, cfg_video: str, video_name: str, qp: int, frames: int = -1):
        vtm_dir = "/home/luispmendes/VVCSoftware_VTM/"

        cfg_dir = vtm_dir + "cfg/"    
        bin_dir = vtm_dir + "bin/"
        out_dir = vtm_dir + "out/"

        if frames == -1:
            frames_encoded = ''
        else:
            frames_encoded = f' -f {frames} '

        print(f'encoding {video_name} with cfg {cfg_encoder}, {cfg_video} and qp {qp}')

        os.system(f'{bin_dir}EncoderAppStatic -c {cfg_dir}{cfg_encoder} \
            -c {cfg_video} -b {out_dir}videos_bin/{video_name}.bin -q {qp}{frames_encoded}>> {out_dir}/logs_execution/log_{video_name}.txt \
            && gprof {bin_dir}EncoderAppStatic gmon.out >> {out_dir}/logs_gprof/gprof_log_{video_name}.txt')


