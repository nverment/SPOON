import os
import sys
import os
import argparse
from mutagen.easyid3 import EasyID3
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(
        description=
        "Rename your music files neatly."
    )

    # required
    parser.add_argument(
        "--dir", 
        # required=True,
        help="Directory where files are stored")

    return parser.parse_args()
    
def process_files(filepath):
    if not os.path.isdir(filepath):
        print("Not a directory. Exiting.")
        exit(1)
    for p in os.listdir(filepath):
        fil = f"{filepath}{p}"
        ddd = p.replace(".mp3", "").split(' - ', 1)
        tag_mp3(fil, ddd[1], ddd[0])

def tag_mp3(path, title, artist, album=None):
    audio = EasyID3(path)
    audio["title"] = title
    audio["artist"] = artist
    if album:
        audio["album"] = album
    audio.save()

    # tag_mp3(
    #     path="todolist/01 - Cycles.mp3",
    #     title="Cycles",
    #     artist="Lili Trifilio",
    # )

def main():
    args = parse_args()

    filepath = args.dir
    print(f"Renaming files in {filepath} ...")
    if filepath:
        process_files(filepath)
    else:
        process_files(os.getcwd())
    print("Done!")

if __name__ == "__main__":
    main()
