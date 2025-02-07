import wave
from pydub import AudioSegment



def checK_riff(file_path):
    try:
        with wave.open(file_path, 'rb') as wav_file:
            print(f"Channels: {wav_file.getnchannels()}")
            print(f"Sample width: {wav_file.getsampwidth()} bytes")
            print(f"Frame rate (Sample rate): {wav_file.getframerate()} Hz")
            print(f"Compression type: {wav_file.getcomptype()} - {wav_file.getcompname()}")
            print("is riff")
    except wave.Error as e:
        print(f"Error reading WAV file: {e}")


import subprocess
import wave

def convert_to_riff(input_audio, output_audio):
    """
    Converts an audio file to a proper RIFF WAV format using FFmpeg.
    
    Args:
        input_audio (str): Path to the input audio file.
        output_audio (str): Path to the output RIFF WAV file.
    """
    try:
        # Use FFmpeg to ensure proper RIFF WAV format
        command = [
            "ffmpeg", "-y", "-i", input_audio,
            "-acodec", "pcm_s16le", "-ar", "44100", "-f", "wav", output_audio
        ]
        subprocess.run(command, check=True)

        # Verify RIFF Header
        with wave.open(output_audio, 'rb') as wav_file:
            if wav_file.getcomptype() != 'NONE':
                raise ValueError("The output file is not a valid RIFF WAV format.")
        
        print(f"Successfully converted {input_audio} to proper RIFF WAV: {output_audio}")

    except Exception as e:
        print(f"Error converting {input_audio} to RIFF WAV: {e}")


# Example usage
input_file = "voices/audio.wav"
output_file = "voices/output_riff.wav"
checK_riff(input_file)
convert_to_riff(input_file, output_file)
checK_riff(output_file)
