import sys
import argparse
import json
import runpy

sys.stdout.write("Parsing arguments ...\n")
sys.stdout.flush()

def parse_args():
  desc = "Args from Visions of Code (VoC) to be passed through to Disco Diffusion"
  parser = argparse.ArgumentParser(description=desc)
  parser.add_argument('--settings_path', type=str)

  args = parser.parse_args()
  return args

# retrieves .json 
def get_batch_settings(voc_args):
    batch_settings_path = voc_args.settings_path
    f = open(batch_settings_path, 'r')
    settings = json.load(f)
    return settings

def run_settings_to_args(batch_settings):
    # create a dict

    # iteratively add to it based on object 

def process_batch(batch_settings):
    f = "./disco_diffusion_v5_6.py"
    runs = batch_settings['runs']
    for run_id in runs:
        #print(json.dumps(runs[run_id]))
        run_settings = run_settings_to_args(runs[run_id])
        runpy.run_path(f, init_globals=run_settings)

## main
voc_args=parse_args();
batch_settings=get_batch_settings(voc_args);
#print(batch_settings);

process_batch(batch_settings);