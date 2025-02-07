from __future__ import annotations  # avoid circular import with import py_audio2face
import py_audio2face.audio2face as a2f

import os
from py_audio2face.settings import DEFAULT_PLAYER_INSTANCE

# changing player instance from DEFAULT_PLAYER_INSTANCE to hard coded: player_instance="/World/audio2face/Player"



class _A2FPlayer:
    def set_root_path(self: a2f.Audio2Face, sounds_folder):
        player_instance="/World/audio2face/Player"

        # if is a file, get the folder
        if os.path.isfile(sounds_folder):
            sounds_folder = os.path.dirname(sounds_folder)

        # fix relative paths
        if not os.path.isabs(sounds_folder):
            sounds_folder = os.path.join(os.getcwd(), sounds_folder)

        payload = {
            "a2f_player": player_instance,
            "dir_path": sounds_folder
        }
        print("A2F/Player/SetRootPath")
        print(payload)
        self.post("A2F/Player/SetRootPath", payload=payload)

    def set_track(self: a2f.Audio2Face, input_sound_path: str):
        player_instance="/World/audio2face/Player"
        if not os.path.isfile(input_sound_path):
            raise FileNotFoundError(f"File {input_sound_path} doesn't exist")

        payload = {
            "a2f_player": player_instance,
            "file_name": os.path.basename(input_sound_path),
            "time_range": [0, -1]
        }

        self.post("A2F/Player/SetTrack", payload=payload)

