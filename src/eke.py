import sys
import argparse
import json
import runpy
from operator import itemgetter

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
    args = []
    # destructure batch_settings
    text_prompts, image_prompts = itemgetter(
        'text_prompts',
        'image_prompts'
    )
    args.append('--text_prompts ' + text_prompts)
    args.append('--image_prompts ' + image_prompts)
    return args


def process_batch(batch_settings):
    f = "./disco_diffusion_v5_6.py"
    runs = batch_settings['runs']
    for run_id in runs:
        # print(json.dumps(runs[run_id]))
        run_value = runs[run_id]
        run_args = json.loads(run_value)
        runpy.run_path(f, init_globals=run_args)


# main
voc_args = parse_args()
batch_settings = get_batch_settings(voc_args)
# print(batch_settings);
process_batch(batch_settings)
