import subprocess
import time
from vtube_module import send_parameter_to_vts

# Function to run Rhubarb Lip Sync
def run_rhubarb_lip_sync(audio_file, output_file):
    subprocess.run(["rhubarb", "-f", "json", audio_file, "-o", output_file])

# Function to send phoneme data to VTube Studio
def send_phoneme_data(phonemes_file):
    with open(phonemes_file, "r") as f:
        phonemes = json.load(f)

    phoneme_to_param = {
        "A": "3",   # Open mouth
        "E": "5",  # Smile mouth
        "O": "4",  # Round mouth
        "etc": "MouthNeutral"  # Default neutral mouth
    }

    for event in phonemes["events"]:
        phoneme = event["type"]
        duration = event["duration"] / 1000  # Duration in seconds
        param_id = phoneme_to_param.get(phoneme, "MouthNeutral")
        send_parameter_to_vts(param_id, 1.0)
        time.sleep(duration)
        send_parameter_to_vts(param_id, 0.0)