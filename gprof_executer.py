import os

class gprof_executer:
    def __init__(self, cfg_encoder: str, cfg_video: str, video_name: str, qp: int):
        vtm_dir = "/home/luispmendes/VVCSoftware_VTM/"

        cfg_dir = vtm_dir + "cfg/"    
        bin_dir = vtm_dir + "bin/"
        out_dir = vtm_dir + "out/"

        print(f'encoding {video_name} with cfg {cfg_encoder}, {cfg_video} and qp {qp}')

        os.system(f'{bin_dir}EncoderAppStatic -c {cfg_dir}{cfg_encoder} \
                -c {cfg_video} -b {out_dir}videos_bin/{video_name}.bin -q {qp} -f 32 >> {out_dir}/logs_execution/{cfg_encoder[:-4]}/log_{video_name}_qp{qp}.txt \
                && gprof {bin_dir}EncoderAppStatic gmon.out >> {out_dir}/logs_gprof/{cfg_encoder[:-4]}/gprof_log_{video_name}_qp{qp}.txt')


