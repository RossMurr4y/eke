import sys
import argparse
import json
import runpy

def parse_args():
  desc = "Args from Visions of Code (VoC) to be passed through to Disco Diffusion"
  parser = argparse.ArgumentParser(description=desc)
  parser.add_argument('--prompt', type=str)
  parser.add_argument('--seed', type=int)
  parser.add_argument('--iterations', type=int)
  parser.add_argument('--sizex', type=int)
  parser.add_argument('--sizey', type=int)
  parser.add_argument('--batch_name', type=str)
  parser.add_argument('--update', type=int)
  parser.add_argument('--diffusion_model', type=str)
  parser.add_argument('--use_secondary_model', type=int)
  parser.add_argument('--animation_mode', type=str)
  parser.add_argument('--init_image', type=str)
  parser.add_argument('--init_scale', type=int)
  parser.add_argument('--skip_steps', type=int)
  parser.add_argument('--diffusion_sampling_mode', type=str)
  parser.add_argument('--custom_path', type=str)
  parser.add_argument('--use_checkpoint', type=int)

  parser.add_argument('--ViTB32', type=int)
  parser.add_argument('--ViTB16', type=int)
  parser.add_argument('--ViTL14', type=int)
  parser.add_argument('--ViTL14_336', type=int)
  parser.add_argument('--RN101', type=int)
  parser.add_argument('--RN50', type=int)
  parser.add_argument('--RN50x4', type=int)
  parser.add_argument('--RN50x16', type=int)
  parser.add_argument('--RN50x64', type=int)

  parser.add_argument('--ViTB32_laion2b_e16', type=int)
  parser.add_argument('--ViTB32_laion400m_e31', type=int)
  parser.add_argument('--ViTB32_laion400m_32', type=int)
  parser.add_argument('--ViTB32quickgelu_laion400m_e31', type=int)
  parser.add_argument('--ViTB32quickgelu_laion400m_e32', type=int)
  parser.add_argument('--ViTB16_laion400m_e31', type=int)
  parser.add_argument('--ViTB16_laion400m_e32', type=int)
  parser.add_argument('--RN50_yffcc15m', type=int)
  parser.add_argument('--RN50_cc12m', type=int)
  parser.add_argument('--RN50_quickgelu_yfcc15m', type=int)
  parser.add_argument('--RN50_quickgelu_cc12m', type=int)
  parser.add_argument('--RN101_yfcc15m', type=int)
  parser.add_argument('--RN101_quickgelu_yfcc15m', type=int)
  parser.add_argument('--clip_guidance_scale', type=int)
  parser.add_argument('--tv_scale', type=int)
  parser.add_argument('--range_scale', type=int)
  parser.add_argument('--sat_scale', type=int)
  parser.add_argument('--cutn_batches', type=int)
  parser.add_argument('--skip_augs', type=int)

  parser.add_argument('--video_init_steps', type=int)
  parser.add_argument('--video_init_clip_guidance_scale', type=float)
  parser.add_argument('--video_init_tv_scale', type=float)
  parser.add_argument('--video_init_range_scale', type=float)
  parser.add_argument('--video_init_sat_scale', type=float)
  parser.add_argument('--video_init_cutn_batches', type=int)
  parser.add_argument('--video_init_skip_steps', type=int)
  parser.add_argument('--video_init_path', type=str)
  parser.add_argument('--extract_nth_frame', type=int)
  parser.add_argument('--persistent_frame_output_in_batch_folder', type=int)
  parser.add_argument('--video_init_seed_continuity', type=int)
  parser.add_argument('--video_init_flow_warp', type=int)
  parser.add_argument('--video_init_flow_blend', type=float)
  parser.add_argument('--video_init_check_consistency', type=int)
  parser.add_argument('--video_init_blend_mode', type=str)
  parser.add_argument('--key_frames', type=int)
  parser.add_argument('--max_frames', type=int)
  parser.add_argument('--video_init_frames_scale', type=int)
  parser.add_argument('--video_init_frames_skip_steps', type=str)
  
  parser.add_argument('--midas_weight', type=float)
  parser.add_argument('--near_plane', type=int)
  parser.add_argument('--far_plane', type=int)
  parser.add_argument('--fov', type=int)

  parser.add_argument('--turbo_mode', type=int)
  parser.add_argument('--turbo_steps', type=str)
  parser.add_argument('--turbo_preroll', type=int)

  parser.add_argument('--vr_mode', type=int)
  parser.add_argument('--vr_eye_angle', type=float)
  parser.add_argument('--vr_ipd', type=float)

  parser.add_argument('--frames_scale', type=int)
  parser.add_argument('--frames_skip_steps', type=str)

  parser.add_argument('--perlin_init', type=int)
  parser.add_argument('--perlin_mode', type=str)

  parser.add_argument('--eta', type=float)
  parser.add_argument('--clamp_grad', type=int)
  parser.add_argument('--clamp_max', type=float)

  parser.add_argument('--randomize_class', type=int)
  parser.add_argument('--clip_denoised', type=int)
  parser.add_argument('--fuzzy_prompt', type=int)
  parser.add_argument('--rand_mag', type=float)

  parser.add_argument('--cut_overview', type=str)
  parser.add_argument('--cut_innercut', type=str)
  parser.add_argument('--cut_ic_pow', type=str)
  parser.add_argument('--cut_icgray_p', type=str)

  parser.add_argument('--pad_or_pulp_cut_overview', type=str)
  parser.add_argument('--pad_or_pulp_cut_innercut', type=str)
  parser.add_argument('--pad_or_pulp_cut_ic_pow', type=str)
  parser.add_argument('--pad_or_pulp_cut_icgray_p', type=str)

  parser.add_argument('--watercolor_cut_overview', type=str)
  parser.add_argument('--watercolor_cut_innercut', type=str)
  parser.add_argument('--watercolor_cut_ic_pow', type=str)
  parser.add_argument('--watercolor_cut_icgray_p', type=str)

  parser.add_argument('--resume_run', type=int)
  parser.add_argument('--run_to_resume', type=str)
  parser.add_argument('--resume_from_frame', type=str)
  parser.add_argument('--retain_overwritten_frames', type=int)

  parser.add_argument('--use_vertical_symmetry', type=int)
  parser.add_argument('--use_horizontal_symmetry', type=int)
  parser.add_argument('--transformation_percent', type=float)

  parser.add_argument('--n_batches', type=int)
  parser.add_argument('--force_flow_generation', type=int)
    
  parser.add_argument('--image_file', type=str)
  parser.add_argument('--frame_dir', type=str)

  args = parser.parse_args()
  return args

# retrieves .json 
def get_batch_settings(voc_args):
    batch_settings_path = voc_args.custom_path
    f = open(batch_settings_path)
    data = json.load(f)
    return data

def process_batch(batch_settings):
    f = "./disco_diffusion_v5_6.py"
    for i in batch_settings['runs']:
        runpy.run_path(f, init_globals=i)
        


## main
voc_args=parse_args();
batch_settings=get_batch_settings(voc_args);
process_batch(batch_settings);