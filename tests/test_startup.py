import os
import sys

# Get the absolute path of the project root
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to sys.path
sys.path.insert(0, parent_dir)

print(f"Root directory set to: {os.getcwd()}")

# Now import audio2face
from py_audio2face import audio2face as pya2f

# Test the import
a2f = pya2f.Audio2Face()
print("Audio2Face instance created successfully!")



a2f = pya2f.Audio2Face()

# Generate animation for a single audio file
a2f.audio2face_single(
   audio_file_path="voices/output_riff.wav", #  path of the audio file you want to animate
   output_path="usd/animation.usd",  # path where the animation file will be saved
   fps=60, # frames per second for the animation. Higher fps will result in smoother animations and longer processing time
   emotion_auto_detect=True  # automatically detect emotions in the audio file. If false the set emotion will be used
)

# Generate animation for an entire folder of audio files
# a2f.audio2face_folder(input_folder="path/to/my/folder", output_folder='/output', fps=60)